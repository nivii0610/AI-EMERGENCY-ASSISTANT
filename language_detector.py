try:
    from langdetect import detect
    from langdetect import DetectorFactory
    from langdetect.lang_detect_exception import LangDetectException
    DetectorFactory.seed = 0
except ImportError:
    detect = None
    LangDetectException = ValueError


LANGUAGE_NAMES = {
    "ar": "Arabic",
    "bn": "Bengali",
    "de": "German",
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "gu": "Gujarati",
    "hi": "Hindi",
    "hi_roman": "Hinglish (Hindi)",
    "it": "Italian",
    "kn": "Kannada",
    "ml": "Malayalam",
    "mr": "Marathi",
    "pa": "Punjabi",
    "pt": "Portuguese",
    "ta": "Tamil",
    "ta_roman": "Tanglish (Tamil)",
    "te": "Telugu",
    "te_roman": "Teluglish (Telugu)",
    "ur": "Urdu"
}


def detect_language(text):
    """Return a language code (e.g., 'hi', 'hi_roman', 'ta', 'ta_roman', 'te', 'te_roman', 'en')."""

    if not text or not text.strip():
        return "en"

    text_lower = text.lower().strip()

    # 1. Native script detection (Unicode ranges)
    script_ranges = {
        "ar": ("\u0600", "\u06ff"),
        "bn": ("\u0980", "\u09ff"),
        "gu": ("\u0a80", "\u0aff"),
        "pa": ("\u0a00", "\u0a7f"),
        "ta": ("\u0b80", "\u0bff"),
        "te": ("\u0c00", "\u0c7f"),
        "kn": ("\u0c80", "\u0cff"),
        "ml": ("\u0d00", "\u0d7f"),
        "hi": ("\u0900", "\u097f")
    }

    for language, (start, end) in script_ranges.items():
        if any(start <= character <= end for character in text):
            return language

    # 2. Phonetic / Romanized language detection (Hinglish, Tanglish, Teluglish)
    hinglish_keywords = (
        "thik nhi", "theek nahi", "thik nahi", "mai thik", "me thik", "mujhe",
        "tabiyat", "chot", "khoon", "khun", "dard", "darr", "dar", "madad",
        "bachao", "aag", "paani", "pani", "ho raha", "kar diya", "kardiya",
        "samajh", "samaj", "ho gaya", "kya karu", "kaise", "bimaar", "bimar"
    )

    tanglish_keywords = (
        "nalla illai", "nalla ila", "naan", "enaku", "udhavi", "ratham",
        "kaayam", "bayama", "kaapadunge", "mudiyala", "thee", "thanni",
        "pannittaen", "aachu", "mudinjichu", "seri", "pennunga"
    )

    teluglish_keywords = (
        "bagonu", "baagoledu", "nenu", "naaku", "saayam", "nethuru",
        "dhabba", "bhayamga", "kaapaadandi", "kaavatledhu", "nippu", "neellu",
        "chesanu", "ayipoyindi", "ibbandhi", "noppi"
    )

    if any(kw in text_lower for kw in hinglish_keywords):
        return "hi_roman"

    if any(kw in text_lower for kw in tanglish_keywords):
        return "ta_roman"

    if any(kw in text_lower for kw in teluglish_keywords):
        return "te_roman"

    # 3. Fallback to langdetect if available
    if detect is not None:
        try:
            language = detect(text)
            if language in LANGUAGE_NAMES:
                return language
        except (LangDetectException, RuntimeError, ValueError):
            pass

    return "en"


def language_name(language_code):
    return LANGUAGE_NAMES.get(language_code, "the user's language")

