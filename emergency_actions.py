def get_actions(emergency_type):

    actions = {

        "FLOOD": [
            "Move to a safer elevated location away from rapidly rising water.",
            "Avoid walking or driving through floodwater.",
            "Stay away from electrical equipment in flooded areas.",
            "Follow evacuation instructions from local authorities."
        ],


        "FIRE": [
            "Move away from the fire and smoke.",
            "Leave the building using a safe exit if possible.",
            "Avoid elevators during a building fire.",
            "Follow instructions from firefighters or emergency responders."
        ],


        "EARTHQUAKE": [
            "Protect yourself from falling objects.",
            "Stay away from windows and unstable structures.",
            "After the shaking stops, move to a safer location if possible.",
            "Follow official emergency instructions."
        ],


        "HEATWAVE": [
            "Move to a cool or well-ventilated place.",
            "Drink water regularly if you can safely do so.",
            "Avoid unnecessary strenuous activity during extreme heat.",
            "Follow local heat-health guidance."
        ],


        "CYCLONE / STORM": [
            "Stay indoors and away from windows.",
            "Follow official weather warnings.",
            "Stay away from unsecured objects.",
            "Follow evacuation instructions from local authorities."
        ],


        "ROAD ACCIDENT": [
            "Move away from traffic danger if you can do so safely.",
            "Avoid creating additional danger around the accident.",
            "Seek emergency assistance when necessary.",
            "Follow instructions from trained emergency responders."
        ],


        "MEDICAL": [
            "Stay in a safe location and remain as calm as possible.",
            "Seek professional emergency medical assistance when necessary.",
            "If you cannot get help yourself, ask a nearby person for assistance.",
            "Follow instructions from trained medical responders."
        ]
    }


    return actions.get(
        emergency_type.upper(),
        [
            "Move to a safer location if possible.",
            "Seek help from a nearby person or emergency responder.",
            "Follow official emergency instructions."
        ]
    )

