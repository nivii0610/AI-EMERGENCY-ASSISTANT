from fire_emergency import handle_fire_emergency
from medical_emergency import handle_medical_emergency
from accident_emergency import handle_accident_emergency


def handle_emergency(emergency, user_input):

    emergency = emergency.upper()

    # ==========================================
    # FIRE
    # ==========================================

    if emergency == "FIRE":

        return handle_fire_emergency(
            user_input
        )


    # ==========================================
    # MEDICAL
    # ==========================================

    elif emergency == "MEDICAL":

        return handle_medical_emergency(
            user_input
        )


    # ==========================================
    # ROAD ACCIDENT
    # ==========================================

    elif emergency == "ROAD ACCIDENT":

        return handle_accident_emergency(
            user_input
        )


    # ==========================================
    # FLOOD
    # ==========================================

    elif emergency == "FLOOD":

        return {
            "category":
                "FLOOD EMERGENCY",

            "message":
                "Move to a safer elevated location "
                "if possible and avoid floodwater.",

            "priority":
                "HIGH"
        }


    # ==========================================
    # EARTHQUAKE
    # ==========================================

    elif emergency == "EARTHQUAKE":

        return {
            "category":
                "EARTHQUAKE EMERGENCY",

            "message":
                "Protect yourself from falling objects "
                "and stay away from windows and unstable "
                "structures.",

            "priority":
                "HIGH"
        }


    # ==========================================
    # HEATWAVE
    # ==========================================

    elif emergency == "HEATWAVE":

        return {
            "category":
                "HEATWAVE EMERGENCY",

            "message":
                "Move to a cooler location and drink "
                "water if you can safely do so.",

            "priority":
                "MEDIUM"
        }


    # ==========================================
    # CYCLONE / STORM
    # ==========================================

    elif emergency == "CYCLONE / STORM":

        return {
            "category":
                "CYCLONE / STORM EMERGENCY",

            "message":
                "Stay indoors, away from windows, "
                "and follow official weather warnings.",

            "priority":
                "HIGH"
        }


    # ==========================================
    # UNKNOWN EMERGENCY
    # ==========================================

    else:

        return {
            "category":
                "GENERAL EMERGENCY",

            "message":
                "Move to a safer location if possible "
                "and seek appropriate emergency assistance.",

            "priority":
                "MEDIUM"
        }