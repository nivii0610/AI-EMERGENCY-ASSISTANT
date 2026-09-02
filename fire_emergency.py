def handle_fire_emergency(user_input):

    text = user_input.lower()

    critical_keywords = [
        "trapped",
        "can't escape",
        "cannot escape",
        "unable to escape",
        "unconscious",
        "not breathing"
    ]

    high_keywords = [
        "fire",
        "flames",
        "smoke",
        "burning",
        "building fire"
    ]


    # ==========================================
    # CRITICAL
    # ==========================================

    for keyword in critical_keywords:

        if keyword in text:

            return {
                "category": "FIRE EMERGENCY",
                "priority": "CRITICAL",
                "message":
                    "Move away from fire and smoke if you can "
                    "do so safely and seek emergency assistance."
            }


    # ==========================================
    # HIGH
    # ==========================================

    for keyword in high_keywords:

        if keyword in text:

            return {
                "category": "FIRE EMERGENCY",
                "priority": "HIGH",
                "message":
                    "Move away from fire and smoke and "
                    "follow safe evacuation instructions."
            }


    # ==========================================
    # GENERAL
    # ==========================================

    return {
        "category": "FIRE EMERGENCY",
        "priority": "HIGH",
        "message":
            "Move away from the fire and smoke if possible "
            "and seek appropriate emergency assistance."
    }

