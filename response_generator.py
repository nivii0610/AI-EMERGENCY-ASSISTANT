import json
import os
from urllib.error import URLError
from urllib.request import Request, urlopen
from language_detector import language_name

# ==========================================
# KNOWLEDGE BASE FILE
# ==========================================

KNOWLEDGE_BASE = "emergency_data.json"


# ==========================================
# LOAD EMERGENCY DATA
# ==========================================

def load_emergency_data():
    if not os.path.exists(KNOWLEDGE_BASE):
        return {}

    try:
        with open(
            KNOWLEDGE_BASE,
            "r",
            encoding="utf-8"
        ) as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return {}


# ==========================================
# GET EMERGENCY RESPONSE
# ==========================================

def get_emergency_response(emergency_type):
    emergency_type = emergency_type.upper()
    emergency_data = load_emergency_data()

    if emergency_type in emergency_data:
        return emergency_data[emergency_type]

    return {
        "title": "Unknown Emergency",
        "guidance": [
            "The system could not identify a specific emergency category.",
            "Move to a safer location if possible.",
            "Seek help from a nearby person or appropriate emergency service."
        ],
        "source": "Emergency preparedness knowledge base"
    }


def _generate_with_ollama(prompt):
    host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    model = os.getenv("OLLAMA_MODEL", "llama3.2:3b")

    payload = json.dumps({
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.2}
    }).encode("utf-8")

    request = Request(
        f"{host.rstrip('/')}/api/generate",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urlopen(request, timeout=8) as response:
            result = json.loads(response.read().decode("utf-8"))
        return result.get("response", "").strip()
    except (URLError, TimeoutError, json.JSONDecodeError, OSError):
        return ""


def translate_response(message, language):
    """Translate assistant text while preserving its safety meaning."""
    if not message or language == "en":
        return message

    return _generate_with_ollama(
        "Translate the following emergency instruction into "
        f"language code {language}. Preserve the exact safety meaning. "
        "Use short, natural language and return only the translation.\n\n"
        f"Text: {message}"
    )


def generate_status_response(emergency, instruction, user_status, language="en"):
    """Generate a warm, empathetic human emergency dispatcher reply in the user's language."""

    # 1. Try Ollama LLM if available
    lang_instruction = (
        f"Respond in {language_name(language)}. "
        if language != "en" else "Respond in English. "
    )

    prompt = (
        "You are a calm, empathetic, professional 911 emergency responder on the line with a person in distress. "
        f"{lang_instruction}"
        "Reply in 2 warm, direct sentences. "
        "First sentence: reassuringly acknowledge their emotion or current status (e.g. if they say they are scared or unwell, reassure them with warmth). "
        "Second sentence: give them clear, direct guidance based on the instruction provided. "
        "Do not sound robotic or menu-driven. Speak like a real supportive human dispatcher.\n\n"
        f"Emergency Category: {emergency}\n"
        f"User Said: {user_status}\n"
        f"Current Instruction: {instruction}"
    )

    ollama_res = _generate_with_ollama(prompt)
    if ollama_res:
        return ollama_res

    # 2. Smart Offline Multilingual Empathetic Response Engine (when Ollama is unavailable)
    status_lower = user_status.lower()

    # Detect Fear / Panic / Pain / Distress Cues across languages
    fear_words = (
        "scared", "fear", "afraid", "panic", "panicking", "worried", "worry",
        "terrified", "nervous", "anxious", "crying", "hurt", "hurts", "pain",
        "help me", "frightened", "bloody", "a lot of blood",
        # Hinglish / Hindi
        "darr", "dar", "thik nhi", "theek nahi", "thik nahi", "madad", "bachao", "takleef",
        # Tanglish / Tamil
        "bayama", "nalla illai", "kaapadunge", "udhavi",
        # Teluglish / Telugu
        "bhayamga", "bagonu", "kaapaadandi", "saayam"
    )
    is_fearful = any(word in status_lower for word in fear_words)

    # Detect Inability / Obstacles first
    obstacle_words = (
        "can't", "cannot", "no cloth", "no towel", "unable", "don't have", "dont have",
        "impossible", "hard", "alone", "haven't", "havent", "not able",
        "nahi ho", "nahi hai", "mudiyala", "illa", "kaavatledhu", "ledu"
    )
    is_obstacle = any(word in status_lower for word in obstacle_words)

    # Detect Progress / Completion (only if not an obstacle)
    progress_words = (
        "done", "applied", "holding", "held", "ok", "okay",
        "yes", "did it", "finished", "got it", "i did", "pressing",
        "ho gaya", "kar diya", "pannittaen", "aachu", "chesanu", "ayipoyindi"
    )
    is_progressing = not is_obstacle and any(word in status_lower for word in progress_words)

    reassurance = ""

    # Language-specific empathetic responses
    if language in ("hi", "hi_roman"):
        if is_fearful:
            reassurance = "Aap ghabraiye mat, main aapke saath hoon. Gehri saans lein aur shant rahein."
        elif is_obstacle:
            reassurance = "Koi baat nahi, ghabraiye mat. Hum dusra safe option try karte hain."
        elif is_progressing:
            reassurance = "Bahut badiya, aapne sahi kadam uthaya."
        else:
            reassurance = "Main aapki baat samajh raha hoon. Main aapke saath hoon step by step."

    elif language in ("ta", "ta_roman"):
        if is_fearful:
            reassurance = "Bayamapadadhinga, naan ungalukku udhava inge irukken. Aazhama swasiyunga."
        elif is_obstacle:
            reassurance = "Kavalai padadhinga, vera safe option try pannalam."
        elif is_progressing:
            reassurance = "Nalla vela, sariyana mudivu eduthirukkinga."
        else:
            reassurance = "Naan ungalukku udhava inge irukken step by step."

    elif language in ("te", "te_roman"):
        if is_fearful:
            reassurance = "Kangarupadakandi, nenu meeku sahaayam cheyanu ikkada unnanu. Deep breath theeskondi."
        elif is_obstacle:
            reassurance = "Paravaledhu, em kangarupadakandi. Inko safe option try chedham."
        elif is_progressing:
            reassurance = "Chala manchidi, meeru sariyainadhi chesaaru."
        else:
            reassurance = "Nenu meeku prathi step lo saayam chesthanu."

    else:
        # Default English
        if is_fearful:
            reassurance = "Take a deep breath. It's completely normal to feel scared right now, but you are doing the right thing and I'm right here with you."
        elif is_obstacle:
            reassurance = "That's completely okay, don't worry. Let's try a safer option right away."
        elif is_progressing:
            reassurance = "Good job taking action."
        else:
            reassurance = "I understand. I am right here with you step by step."

    if instruction:
        return f"{reassurance} {instruction}"
    return reassurance