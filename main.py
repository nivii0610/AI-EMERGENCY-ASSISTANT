import sys
import webbrowser

# Enable UTF-8 encoding for Windows terminals
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from voice_input import get_voice_input
from voice_output import speak

from semantic_search import find_similar_emergency
from emergency_detector import detect_emergency
from severity_detector import detect_severity

from emergency_state_machine import EmergencyStateMachine
from emergency_response_manager import get_emergency_response_action
from location_handler import get_location
from location_handler import format_location

from emergency_logger import log_emergency
from alert_system import generate_alert
from response_generator import generate_status_response, translate_response
from language_detector import detect_language
from offline_mode import show_offline_status

CURRENT_LANGUAGE = "en"


def choose_interaction_mode():
    while True:
        print("\nHow would you like to use the assistant?")
        print("1. Chat (type your answers)")
        print("2. Voice (speak your answers)")

        choice = input("Choose Chat or Voice: ").strip().lower()

        if choice in ("1", "chat", "c"):
            return "chat"
        if choice in ("2", "voice", "v"):
            return "voice"

        print("Please choose Chat or Voice.")


def respond(message, mode):
    translated_message = translate_response(message, CURRENT_LANGUAGE)
    if translated_message:
        message = translated_message

    if mode == "voice":
        speak(message)
    else:
        print(f"\nAssistant: {message}", flush=True)


def ask(question, mode, announce=True):
    if mode == "voice":
        return get_voice_input(question)

    if announce:
        respond(question, mode)

    return input("You: ").strip()


def ask_situation_details(user_input, emergency, mode):
    text = user_input.lower()
    questions = {
        "FIRE": (
            "I'm so sorry you're dealing with this. Are you in a safe room right now, "
            "is smoke making breathing difficult, or can you reach a safe exit?"
        ),
        "FLOOD": (
            "Stay calm, I am right here with you. Is the floodwater rising around you, "
            "and are you able to reach higher ground safely?"
        ),
        "EARTHQUAKE": (
            "Take cover and protect yourself right now. Is the shaking continuing, "
            "or is anyone injured or trapped?"
        ),
        "ROAD ACCIDENT": (
            "Stay safe and away from traffic. Is anyone trapped, unconscious, "
            "bleeding heavily, or in immediate danger?"
        ),
        "CYCLONE / STORM": (
            "Stay sheltered indoors. Is there structural damage or rising water around you?"
        ),
        "HEATWAVE": (
            "I'm here to help. Is anyone feeling confused, fainting, having trouble breathing, "
            "or unable to stay hydrated?"
        ),
        "MEDICAL": (
            "I'm right here with you. Is anyone unconscious, having trouble breathing, "
            "bleeding heavily, or in severe pain?"
        )
    }

    question = questions.get(
        emergency,
        "Is anyone injured, trapped, or in immediate danger?"
    )

    response = ask(question, mode)

    if response:
        return f"{user_input}. Follow-up details: {response}"

    return user_input


def request_emergency_call(service_action, mode):
    answer = ask(
        f"This situation sounds critical. Would you like me to open a direct call to "
        f"{service_action['service']} at {service_action['number']} right now?",
        mode
    ).lower()

    if answer not in ("yes", "y", "yeah", "okay", "ok", "please", "do it", "sure", "haan", "aama", "avunu"):
        respond(
            f"Understood. If you need help, please call {service_action['number']} "
            "directly or ask someone nearby to call for you.",
            mode
        )
        return

    opened = webbrowser.open(
        f"tel:{service_action['number']}"
    )

    if opened:
        respond(
            f"I have opened the dialer for {service_action['service']}. "
            "Please press call to connect immediately.",
            mode
        )
    else:
        respond(
            f"I couldn't open the phone dialer automatically on this device. "
            f"Please call {service_action['number']} for {service_action['service']} immediately.",
            mode
        )


def main():
    global CURRENT_LANGUAGE

    print("\n===================================")
    print("AI EMERGENCY ASSISTANT")
    print("===================================")

    mode = choose_interaction_mode()
    show_offline_status()

    respond(
        "Hello, I am your AI Emergency Assistant. I am right here to help you stay safe.",
        mode
    )

    # -----------------------------------
    # STEP 1: GET EMERGENCY FROM VOICE / CHAT
    # -----------------------------------

    user_input = ask("Please tell me what emergency is happening.", mode)

    if not user_input:
        respond(
            "I didn't catch that. Please tell me what emergency is happening.",
            mode
        )
        user_input = ask("Please describe it again.", mode)

    if not user_input:
        respond(
            "I couldn't receive your details. Please reach out to emergency services or someone nearby immediately.",
            mode
        )
        return

    CURRENT_LANGUAGE = detect_language(user_input)

    # -----------------------------------
    # STEP 2: AI EMERGENCY DETECTION
    # -----------------------------------

    detected_emergency = detect_emergency(user_input)

    if detected_emergency == "UNKNOWN":
        emergency, similarity = find_similar_emergency(user_input)
    else:
        emergency = detected_emergency
        similarity = 1.0

    user_input = ask_situation_details(user_input, emergency, mode)

    # -----------------------------------
    # STEP 3: SEVERITY DETECTION
    # -----------------------------------

    severity = detect_severity(
        user_input,
        similarity
    )

    service_action = get_emergency_response_action(
        emergency,
        severity
    )

    if severity == "CRITICAL":
        request_emergency_call(service_action, mode)

    call_requested = severity == "CRITICAL"

    state_machine = EmergencyStateMachine(
        emergency,
        user_input
    )

    # First instruction greeting turn
    first_instruction = state_machine.get_instruction()

    # Generate localized initial greeting + instruction
    initial_greeting = generate_status_response(emergency, first_instruction, user_input, CURRENT_LANGUAGE)
    respond(initial_greeting, mode)

    # Interactive responder loop
    while not state_machine.is_finished():
        answer = ask(
            "",
            mode,
            announce=False
        )

        if not answer:
            respond("Take your time. Please let me know how you're doing or if you need help.", mode)
            continue

        answer_lower = answer.lower().strip()
        user_input = f"{user_input}. New information: {answer_lower}"
        severity = detect_severity(user_input, 1.0)

        # Update language dynamically if user switches language mid-chat
        new_lang = detect_language(answer)
        if new_lang != "en":
            CURRENT_LANGUAGE = new_lang

        changed_emergency = detect_emergency(answer_lower)
        if changed_emergency != "UNKNOWN" and changed_emergency != emergency:
            emergency = changed_emergency
            severity = detect_severity(user_input, 1.0)
            service_action = get_emergency_response_action(
                emergency,
                severity
            )
            state_machine = EmergencyStateMachine(
                emergency,
                user_input
            )
            if severity == "CRITICAL" and not call_requested:
                request_emergency_call(service_action, mode)
                call_requested = True
            respond(f"I understand. Let's adjust: {state_machine.get_instruction()}", mode)
            continue

        if severity == "CRITICAL" and not call_requested:
            service_action = get_emergency_response_action(
                emergency,
                severity
            )
            request_emergency_call(service_action, mode)
            call_requested = True

        # -----------------------------------
        # NATURAL INTENT PARSING (MULTILINGUAL)
        # -----------------------------------

        # 1. HELP / UNSAFE / DISTRESS
        help_words = (
            "help", "not safe", "unsafe", "need help", "someone help",
            "danger", "worse", "getting worse", "can't escape", "trapped",
            "madad", "bachao", "khatra", "madad karo", "bachaao",
            "udhavi", "kaapadunge", "abayam", "udhavi venum",
            "saayam", "kaapaadandi", "pramadam", "saayam kaavali"
        )
        if any(word in answer_lower for word in help_words):
            respond(
                "Please move to a safer location immediately if you can do so safely. "
                "Contact emergency services right away at 112 or ask someone nearby to assist you.",
                mode
            )
            continue

        # 2. CANNOT DO / OBSTACLE
        cannot_words = (
            "cannot", "can't", "cant", "unable", "cannot do", "can't do",
            "not possible", "no cloth", "no towel", "don't have", "impossible", "hard",
            "nahi ho raha", "nahi hai", "nahi kar sakta", "nahi kar pa raha", "kapda nahi hai",
            "mudiyala", "illa", "panna mudiyala", "towel illa",
            "kaavatledhu", "ledu", "cheyaleenu", "towel ledu"
        )
        if any(word in answer_lower for word in cannot_words):
            alternative = state_machine.get_alternative()
            respond(
                f"That's completely okay, don't force it. Try this safer alternative: {alternative}",
                mode
            )
            continue

        # 3. STEP COMPLETED / PROGRESS
        done_words = (
            "done", "yes", "i did it", "finished", "reached", "completed",
            "okay", "ok", "applied", "holding", "held", "got towel", "got cloth",
            "pressing", "did that", "done that", "yep", "yeah", "i have",
            "ho gaya", "kar diya", "kardiya", "haan", "thik hai", "hogaya", "ho gya",
            "pannittaen", "aachu", "aama", "seri", "mudinjichu",
            "chesanu", "ayipoyindi", "avunu", "sare"
        )
        if any(word in answer_lower for word in done_words):
            state_machine.mark_step_complete()
            if not state_machine.is_finished():
                next_inst = state_machine.get_instruction()
                step_res = generate_status_response(emergency, next_inst, answer, CURRENT_LANGUAGE)
                respond(step_res, mode)
            continue

        # 4. EMOTIONAL / GENERAL STATUS RESPONSE (e.g. "im scared", "me thik nhi hu")
        current_inst = state_machine.get_instruction()
        generated_response = generate_status_response(
            emergency,
            current_inst,
            answer,
            CURRENT_LANGUAGE
        )

        if generated_response:
            respond(generated_response, mode)
        else:
            respond(
                f"I'm right here with you. Take a deep breath. {current_inst}",
                mode
            )

    # -----------------------------------
    # GUIDANCE COMPLETE & LOCATION LOGGING
    # -----------------------------------
    respond("The immediate safety guidance is complete.", mode)

    location = get_location()
    location_text = format_location(location)

    generate_alert(
        emergency,
        severity,
        user_input,
        location_text
    )

    log_emergency(
        emergency,
        severity,
        user_input,
        location_text,
        similarity
    )

    respond(
        "Your emergency information has been recorded. Please stay safe and follow instructions from emergency responders.",
        mode
    )

    print("\n===================================")
    print("✅ EMERGENCY SESSION COMPLETE")
    print("===================================")


if __name__ == "__main__":
    main()
