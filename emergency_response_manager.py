def get_emergency_response_action(emergency, severity):

    emergency = emergency.upper()
    severity = severity.upper()


    # ==========================================
    # CRITICAL EMERGENCY
    # ==========================================

    if severity == "CRITICAL":

        if emergency == "FIRE":

            return {
                "service": "Fire and Emergency Service",
                "number": "112 / 101",
                "action":
                    "This is a critical fire emergency. "
                    "Emergency assistance may be required."
            }


        elif emergency == "MEDICAL":

            return {
                "service": "Ambulance / Emergency Medical Service",
                "number": "112 / 102",
                "action":
                    "This is a critical medical emergency. "
                    "Emergency medical assistance may be required."
            }


        elif emergency == "FLOOD":

            return {
                "service": "Emergency / Disaster Response",
                "number": "112",
                "action":
                    "This is a critical flood emergency. "
                    "Emergency assistance may be required."
            }


        elif emergency == "ROAD ACCIDENT":

            return {
                "service": "Emergency Service",
                "number": "112",
                "action":
                    "This is a critical road accident. "
                    "Emergency assistance may be required."
            }


        else:

            return {
                "service": "National Emergency Service",
                "number": "112",
                "action":
                    "This is a critical emergency. "
                    "Emergency assistance may be required."
            }


    # ==========================================
    # MEDIUM EMERGENCY
    # ==========================================

    elif severity == "MEDIUM":

        return {
            "service":
                "Emergency assistance if the situation worsens",

            "number":
                "112",

            "action":
                "Follow the safety instructions carefully "
                "and monitor the situation."
        }


    # ==========================================
    # LOW EMERGENCY
    # ==========================================

    else:

        return {
            "service":
                "No emergency call recommended",

            "number":
                "N/A",

            "action":
                "Follow the provided safety guidance."
        }

