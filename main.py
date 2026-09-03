from voice_input import get_voice_input
from voice_output import speak

from semantic_search import find_similar_emergency
from severity_detector import detect_severity

from emergency_state_machine import EmergencyStateMachine
from response_generator import generate_status_response

from emergency_response_manager import (
    get_emergency_response_action
)

from emergency_logger import log_emergency
from alert_system import generate_alert

from offline_mode import show_offline_status


def chat_output(text):

    print("\nAssistant:")
    print(text)


def chat_input(prompt=""):

    return input(f"\nAssistant: {prompt}\nYou: ").strip()


# ==========================================
# START ASSISTANT
# ==========================================

print("===================================")
print("      AI EMERGENCY ASSISTANT")
print("===================================")

while True:

    input_mode = input("Choose chat or voice: ").strip().lower()

    if input_mode in ("chat", "c"):
        speak = chat_output
        get_input = chat_input
        break

    if input_mode in ("voice", "v"):
        get_input = get_voice_input
        break

    print("Please enter chat or voice.")


show_offline_status()


speak(
    "Hello. I am your emergency assistant. "
    "Stay calm and tell me what happened."
)


# ==========================================
# STEP 1: GET EMERGENCY
# ==========================================

user_input = get_input(
    "Tell me what happened."
)


if not user_input:

    speak(
        "I could not understand you. "
        "Please describe the emergency again."
    )

    user_input = get_input(
        "Please tell me what happened."
    )


if not user_input:

    speak(
        "I could not receive your emergency information. "
        "Please seek help from a nearby person or emergency service."
    )

    exit()


# ==========================================
# STEP 2: DETECT EMERGENCY
# ==========================================

emergency, similarity = find_similar_emergency(
    user_input
)


print("\n===================================")
print("Detected Emergency:", emergency)
print("AI Similarity Score:", round(similarity, 2))
print("===================================")


speak(
    f"I detected a possible {emergency.lower()} emergency."
)


# ==========================================
# STEP 3: DETECT SEVERITY
# ==========================================

severity = detect_severity(
    user_input,
    similarity
)


print("Severity:", severity)


speak(
    f"The detected severity is {severity.lower()}."
)


# ==========================================
# STEP 4: EMERGENCY SERVICE INFORMATION
# ==========================================

response_action = get_emergency_response_action(
    emergency,
    severity
)


print("\n🚨 EMERGENCY RESPONSE")
print("-----------------------------------")
print("Service:", response_action["service"])
print("Number:", response_action["number"])
print("Action:", response_action["action"])


speak(
    response_action["action"]
)


# ==========================================
# STEP 5: CREATE GUIDANCE SYSTEM
# ==========================================

assistant = EmergencyStateMachine(
    emergency,
    user_input
)


speak(
    "I will guide you one step at a time. "
    "You only need to speak to me."
)

# Carries the person's most recent words forward so the very first
# instruction can acknowledge how they described things initially,
# and each later instruction reacts to what they just said (scared,
# stuck, or making progress) instead of repeating a generic line.
last_status = user_input


# ==========================================
# STEP 6: STEP-BY-STEP GUIDANCE
# ==========================================

while not assistant.is_finished():

    progress = assistant.get_progress()

    instruction = assistant.get_instruction()

    alternative = assistant.get_alternative()


    print("\n===================================")

    print(
        f"STEP {progress['current_step']} "
        f"OF {progress['total_steps']}"
    )

    print("===================================")


    # --------------------------------------
    # GIVE ONE INSTRUCTION (with empathy)
    # --------------------------------------

    speak(
        generate_status_response(
            emergency,
            instruction,
            last_status
        )
    )


    # --------------------------------------
    # ASK FOR STATUS
    # --------------------------------------

    answer = get_input(
        "Tell me if you completed the step, "
        "cannot do it, or need help."
    )


    if not answer:

        speak(
            "I could not understand your response."
        )

        continue


    answer = answer.lower().strip()


    # ======================================
    # HELP / NOT SAFE
    # CHECK THIS FIRST
    # ======================================

    help_words = [

        "help",
        "i need help",
        "save me",
        "i'm in danger",
        "im in danger",
        "i am in danger",
        "not safe",
        "i'm not safe",
        "im not safe",
        "i am not safe",
        "someone help"
    ]


    if any(word in answer for word in help_words):

        last_status = answer

        speak(
            "I understand that you need immediate help."
        )

        speak(
            "Please contact the appropriate emergency "
            "service using the emergency number provided."
        )

        speak(
            "If you cannot make the call yourself, "
            "ask a nearby person to contact emergency services."
        )

        continue


    # ======================================
    # CANNOT COMPLETE STEP
    # ======================================

    cannot_words = [

        "can't",
        "cannot",
        "unable",
        "not possible",
        "blocked",
        "i can't do it",
        "i cannot do it",
        "i can't",
        "i cannot"
    ]


    if any(word in answer for word in cannot_words):

        last_status = answer

        speak(
            generate_status_response(
                emergency,
                alternative,
                answer
            )
        )

        continue


    # ======================================
    # STEP COMPLETED
    # ======================================

    completed_words = [

        "done",
        "completed",
        "reached",
        "yes",
        "okay",
        "ok",
        "finished",
        "i did it",
        "i'm there",
        "im there",
        "i reached",
        "i am there"
    ]


    if any(word in answer for word in completed_words):

        last_status = answer
        assistant.mark_step_complete()

        # No speak() here on purpose: the next loop iteration calls
        # generate_status_response() with this "done" status, which
        # already produces a warm "good job, here's what's next" line
        # right before the next instruction, so we don't say it twice.

        continue


    # ======================================
    # UNCLEAR RESPONSE
    # ======================================

    speak(
        "I did not understand."
    )

    speak(
        "You can say done, I cannot, or I need help."
    )


# ==========================================
# STEP 7: GUIDANCE COMPLETE
# ==========================================

print("\n===================================")
print("ALL GUIDANCE STEPS COMPLETED")
print("===================================")


speak(
    "You have completed the immediate guidance steps."
)


# ==========================================
# STEP 8: CREATE ALERT
# ==========================================

location = "GPS location currently unavailable"


generate_alert(
    emergency,
    severity,
    user_input,
    location
)


# ==========================================
# STEP 9: SAVE EMERGENCY LOG
# ==========================================

log_emergency(
    emergency,
    severity,
    user_input,
    location,
    similarity
)


# ==========================================
# FINISH
# ==========================================

speak(
    "The immediate emergency guidance session is complete. "
    "Continue following instructions from official emergency responders."
)


print("\n===================================")
print("      ASSISTANT SESSION COMPLETE")
print("===================================")
