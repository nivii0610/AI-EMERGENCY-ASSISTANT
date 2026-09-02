from voice_input import get_voice_input
from voice_output import speak


def confirm_emergency(emergency, severity, location):

    # ==========================================
    # EMERGENCY INFORMATION
    # ==========================================

    speak(
        f"This is a {severity.lower()} "
        f"{emergency.lower()} emergency."
    )

    speak(
        f"Your current location is {location}."
    )


    # ==========================================
    # ASK FOR CONFIRMATION
    # ==========================================

    speak(
        "Emergency assistance may be required."
    )

    speak(
        "Do you want to request emergency assistance? "
        "Please say yes or no."
    )


    # ==========================================
    # LISTEN FOR ANSWER
    # ==========================================

    while True:

        answer = get_voice_input(
            "Please say yes or no."
        )


        if not answer:

            speak(
                "I could not understand you. "
                "Please say yes or no."
            )

            continue


        answer = answer.lower().strip()


        # ======================================
        # YES
        # ======================================

        yes_words = [
            "yes",
            "yeah",
            "yep",
            "yes please",
            "please do",
            "do it"
        ]


        if any(word in answer for word in yes_words):

            speak(
                "Emergency assistance has been requested."
            )

            # IMPORTANT:
            # This currently only records the request.
            # It does NOT automatically call emergency services.

            return True


        # ======================================
        # NO
        # ======================================

        no_words = [
            "no",
            "nope",
            "not now",
            "don't",
            "do not"
        ]


        if any(word in answer for word in no_words):

            speak(
                "Okay. Emergency assistance was not requested."
            )

            return False


        # ======================================
        # UNCLEAR
        # ======================================

        speak(
            "I did not understand your answer."
        )

        speak(
            "Please say yes or no."
        )

