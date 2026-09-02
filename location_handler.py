from gps_location import get_gps_location
from gps_location import get_location_text


# ==========================================
# GET CURRENT LOCATION
# ==========================================

def get_location():

    print("\n📍 LOCATION")
    print("-----------------------------------")

    location = get_gps_location()

    if location is None:

        print(
            "⚠️ GPS location is currently unavailable."
        )

        return None

    print(
        "📍 Current location:",
        get_location_text(location)
    )

    return location


# ==========================================
# FORMAT LOCATION
# ==========================================

def format_location(location):

    if location is None:

        return "Location unavailable"

    return get_location_text(location)