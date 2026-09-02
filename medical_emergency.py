def handle_medical_emergency(user_input):

    text = user_input.lower()


    critical_keywords = [
        "unconscious",
        "not breathing",
        "can't breathe",
        "cannot breathe",
        "severe bleeding",
        "collapsed",
        "unresponsive"
    ]


    # ==========================================
    # CRITICAL
    # ==========================================

    for keyword in critical_keywords:

        if keyword in text:

            return {
                "category": "MEDICAL EMERGENCY",
                "priority": "CRITICAL",
                "message":
                    "This may be a critical medical emergency. "
                    "Seek professional emergency medical assistance immediately."
            }


    # ==========================================
    # GENERAL MEDICAL
    # ==========================================

    return {
        "category": "MEDICAL EMERGENCY",
        "priority": "HIGH",
        "message":
            "Seek professional medical assistance and "
            "follow instructions from trained responders."
    }
