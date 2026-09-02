EMERGENCY_CONTACTS = {

    "GENERAL": {
        "name": "National Emergency Service",
        "number": "112"
    },

    "FIRE": {
        "name": "Fire and Emergency Service",
        "number": "112 / 101"
    },

    "MEDICAL": {
        "name": "Ambulance / Emergency Medical Service",
        "number": "112 / 102"
    },

    "FLOOD": {
        "name": "Emergency / Disaster Response",
        "number": "112"
    },

    "ROAD ACCIDENT": {
        "name": "Emergency Service",
        "number": "112"
    },

    "EARTHQUAKE": {
        "name": "National Emergency Service",
        "number": "112"
    },

    "HEATWAVE": {
        "name": "Emergency Service",
        "number": "112"
    },

    "CYCLONE / STORM": {
        "name": "Emergency / Disaster Response",
        "number": "112"
    }
}


# ==========================================
# GET EMERGENCY CONTACT
# ==========================================

def get_emergency_contact(emergency):

    emergency = emergency.upper()

    return EMERGENCY_CONTACTS.get(
        emergency,
        EMERGENCY_CONTACTS["GENERAL"]
    )


# ==========================================
# DISPLAY EMERGENCY CONTACT
# ==========================================

def show_emergency_contact(emergency):

    contact = get_emergency_contact(
        emergency
    )

    print("\n📞 EMERGENCY CONTACT")
    print("-----------------------------------")

    print(
        "Service:",
        contact["name"]
    )

    print(
        "Number:",
        contact["number"]
    )

    return contact