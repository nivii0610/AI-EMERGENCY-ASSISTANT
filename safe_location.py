import math


# ==========================================
# DEMO SAFE LOCATIONS
# ==========================================
# These are SAMPLE locations for project testing.
# They are NOT verified real emergency shelters
# or hospitals.

SAFE_LOCATIONS = [

    {
        "name": "Demo Emergency Shelter",
        "type": "Shelter",
        "latitude": 13.0827,
        "longitude": 80.2707
    },

    {
        "name": "Demo Medical Centre",
        "type": "Hospital",
        "latitude": 13.0674,
        "longitude": 80.2376
    },

    {
        "name": "Demo Relief Centre",
        "type": "Relief Centre",
        "latitude": 13.0475,
        "longitude": 80.2824
    }
]


# ==========================================
# CALCULATE DISTANCE
# ==========================================

def calculate_distance(
    user_latitude,
    user_longitude,
    location_latitude,
    location_longitude
):

    """
    Calculate approximate distance between
    two GPS coordinates in kilometres.
    """

    earth_radius = 6371

    lat1 = math.radians(user_latitude)
    lat2 = math.radians(location_latitude)

    delta_lat = math.radians(
        location_latitude - user_latitude
    )

    delta_lon = math.radians(
        location_longitude - user_longitude
    )

    a = (
        math.sin(delta_lat / 2) ** 2
        +
        math.cos(lat1)
        * math.cos(lat2)
        * math.sin(delta_lon / 2) ** 2
    )

    c = 2 * math.atan2(
        math.sqrt(a),
        math.sqrt(1 - a)
    )

    return earth_radius * c


# ==========================================
# FIND NEARBY SAFE LOCATIONS
# ==========================================

def find_nearby_safe_locations(
    user_latitude,
    user_longitude,
    emergency_type
):

    emergency_type = emergency_type.upper()

    suitable_locations = []


    # ==========================================
    # SELECT SUITABLE TYPES
    # ==========================================

    if emergency_type == "MEDICAL":

        allowed_types = [
            "Hospital"
        ]

    elif emergency_type in [
        "FLOOD",
        "CYCLONE / STORM"
    ]:

        allowed_types = [
            "Shelter",
            "Relief Centre"
        ]

    else:

        allowed_types = [
            "Shelter",
            "Hospital",
            "Relief Centre"
        ]


    # ==========================================
    # CALCULATE DISTANCE
    # ==========================================

    for location in SAFE_LOCATIONS:

        if location["type"] not in allowed_types:

            continue

        distance = calculate_distance(
            user_latitude,
            user_longitude,
            location["latitude"],
            location["longitude"]
        )

        location_copy = location.copy()

        location_copy["distance_km"] = round(
            distance,
            2
        )

        suitable_locations.append(
            location_copy
        )


    # ==========================================
    # SORT BY DISTANCE
    # ==========================================

    suitable_locations.sort(
        key=lambda location:
        location["distance_km"]
    )

    return suitable_locations


# ==========================================
# DISPLAY LOCATIONS
# ==========================================

def display_safe_locations(locations):

    print("\n🏠 NEARBY LOCATIONS")
    print("===================================")

    if not locations:

        print(
            "No suitable location found."
        )

        return


    for location in locations:

        print(
            "\nName:",
            location["name"]
        )

        print(
            "Type:",
            location["type"]
        )

        print(
            "Distance:",
            location["distance_km"],
            "km"
        )

        print(
            "Coordinates:",
            location["latitude"],
            location["longitude"]
        )