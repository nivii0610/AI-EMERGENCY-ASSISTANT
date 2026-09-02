def get_special_response(emergency, severity):

    emergency = emergency.upper()
    severity = severity.upper()

    # ==========================================
    # FIRE
    # ==========================================

    if emergency == "FIRE":

        return {
            "category": "FIRE EMERGENCY",
            "priority": severity,
            "message":
                "Move away from fire and smoke and "
                "follow safe evacuation instructions.",
            "service":
                "Fire and Emergency Service"
        }


    # ==========================================
    # FLOOD
    # ==========================================

    elif emergency == "FLOOD":

        return {
            "category": "FLOOD EMERGENCY",
            "priority": severity,
            "message":
                "Move to a safer elevated location if "
                "possible and avoid floodwater.",
            "service":
                "Emergency / Disaster Response"
        }


    # ==========================================
    # MEDICAL
    # ==========================================

    elif emergency == "MEDICAL":

        return {
            "category": "MEDICAL EMERGENCY",
            "priority": severity,
            "message":
                "Seek professional medical assistance "
                "when necessary.",
            "service":
                "Ambulance / Emergency Medical Service"
        }


    # ==========================================
    # ROAD ACCIDENT
    # ==========================================

    elif emergency == "ROAD ACCIDENT":

        return {
            "category": "ROAD ACCIDENT",
            "priority": severity,
            "message":
                "Move away from traffic danger if it is "
                "safe to do so and seek emergency assistance.",
            "service":
                "Emergency Service"
        }


    # ==========================================
    # EARTHQUAKE
    # ==========================================

    elif emergency == "EARTHQUAKE":

        return {
            "category": "EARTHQUAKE EMERGENCY",
            "priority": severity,
            "message":
                "Protect yourself from falling objects "
                "and stay away from windows and unstable structures.",
            "service":
                "National Emergency Service"
        }


    # ==========================================
    # HEATWAVE
    # ==========================================

    elif emergency == "HEATWAVE":

        return {
            "category": "HEATWAVE EMERGENCY",
            "priority": severity,
            "message":
                "Move to a cooler location and reduce "
                "exposure to extreme heat.",
            "service":
                "Emergency Service"
        }


    # ==========================================
    # CYCLONE / STORM
    # ==========================================

    elif emergency == "CYCLONE / STORM":

        return {
            "category": "CYCLONE / STORM EMERGENCY",
            "priority": severity,
            "message":
                "Stay indoors, away from windows, "
                "and follow official weather warnings.",
            "service":
                "Emergency / Disaster Response"
        }


    # ==========================================
    # GENERAL EMERGENCY
    # ==========================================

    else:

        return {
            "category": "GENERAL EMERGENCY",
            "priority": severity,
            "message":
                "Follow the safety instructions provided "
                "and seek appropriate emergency assistance.",
            "service":
                "National Emergency Service"
        }