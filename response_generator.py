import json
import os


# ==========================================
# KNOWLEDGE BASE FILE
# ==========================================

KNOWLEDGE_BASE = "emergency_data.json"


# ==========================================
# LOAD EMERGENCY DATA
# ==========================================

def load_emergency_data():

    if not os.path.exists(KNOWLEDGE_BASE):

        return {}

    try:

        with open(
            KNOWLEDGE_BASE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except (json.JSONDecodeError, OSError):

        return {}


# ==========================================
# GET EMERGENCY RESPONSE
# ==========================================

def get_emergency_response(emergency_type):

    emergency_type = emergency_type.upper()

    emergency_data = load_emergency_data()


    # ==========================================
    # EMERGENCY FOUND
    # ==========================================

    if emergency_type in emergency_data:

        return emergency_data[emergency_type]


    # ==========================================
    # EMERGENCY NOT FOUND
    # ==========================================

    return {

        "title": "Unknown Emergency",

        "guidance": [

            "The system could not identify "
            "a specific emergency category.",

            "Move to a safer location if possible.",

            "Seek help from a nearby person "
            "or appropriate emergency service."

        ],

        "source":
            "Emergency preparedness knowledge base"

    }