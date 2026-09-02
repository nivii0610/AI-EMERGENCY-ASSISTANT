def handle_accident_emergency(user_input):

    text = user_input.lower()


    critical_keywords = [
        "trapped in vehicle",
        "trapped inside",
        "unconscious",
        "not breathing",
        "severe bleeding"
    ]


    high_keywords = [
        "accident",
        "crash",
        "collision",
        "car accident",
        "bike accident",
        "vehicle accident"
    ]


    # ==========================================
    # CRITICAL
    # ==========================================

    for keyword in critical_keywords:

        if keyword in text:

            return {
                "category": "ROAD ACCIDENT",
                "priority": "CRITICAL",
                "message":
                    "This may be a critical road accident. "
                    "Seek emergency assistance immediately."
            }


    # ==========================================
    # HIGH
    # ==========================================

    for keyword in high_keywords:

        if keyword in text:

            return {
                "category": "ROAD ACCIDENT",
                "priority": "HIGH",
                "message":
                    "Move away from traffic danger if you can "
                    "do so safely and seek emergency assistance."
            }


    # ==========================================
    # GENERAL
    # ==========================================

    return {
        "category": "ROAD ACCIDENT",
        "priority": "HIGH",
        "message":
            "Move away from traffic danger if possible "
            "and seek appropriate emergency assistance."
    }
