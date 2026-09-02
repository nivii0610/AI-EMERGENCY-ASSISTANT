def detect_severity(user_input, similarity):

    text = user_input.lower()


    # ==========================================
    # CRITICAL EMERGENCY
    # ==========================================

    critical_keywords = [

        "trapped",
        "unconscious",
        "not breathing",
        "can't breathe",
        "cannot breathe",
        "severe bleeding",
        "major accident",
        "building collapse",
        "people trapped",
        "life threatening",
        "life-threatening",
        "collapsed",
        "unresponsive",
        "can't escape",
        "cannot escape"
    ]


    for keyword in critical_keywords:

        if keyword in text:

            return "CRITICAL"


    # ==========================================
    # HIGH-RISK SITUATIONS
    # ==========================================

    high_keywords = [

        "fire",
        "flames",
        "heavy smoke",
        "water entering house",
        "water rising",
        "rapidly rising water",
        "flooding",
        "crash",
        "collision",
        "vehicle accident",
        "road accident",
        "medical emergency",
        "cyclone",
        "strong winds",
        "earthquake",
        "building shaking"
    ]


    for keyword in high_keywords:

        if keyword in text:

            return "HIGH"


    # ==========================================
    # MEDIUM EMERGENCY
    # ==========================================

    medium_keywords = [

        "injured",
        "injury",
        "smoke",
        "flood",
        "accident",
        "gas leak",
        "earthquake",
        "heatwave",
        "extreme heat",
        "storm",
        "danger"
    ]


    for keyword in medium_keywords:

        if keyword in text:

            return "MEDIUM"


    # ==========================================
    # AI SIMILARITY
    # ==========================================

    if similarity >= 0.80:

        return "MEDIUM"


    # ==========================================
    # LOW
    # ==========================================

    return "LOW"

