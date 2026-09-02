# ==========================================
# CREATE GPS LOCATION
# ==========================================

def create_location(latitude, longitude):

    """
    Create and validate a GPS location.
    """

    try:

        latitude = float(latitude)
        longitude = float(longitude)

    except (ValueError, TypeError):

        return None


    # ==========================================
    # VALIDATE COORDINATES
    # ==========================================

    if not -90 <= latitude <= 90:

        return None

    if not -180 <= longitude <= 180:

        return None


    return {
        "latitude": latitude,
        "longitude": longitude
    }


# ==========================================
# FORMAT LOCATION
# ==========================================

def get_location_text(location):

    if location is None:

        return "Location unavailable"

    return (
        f"Latitude: {location['latitude']:.6f}, "
        f"Longitude: {location['longitude']:.6f}"
    )


# ==========================================
# GOOGLE MAPS LINK
# ==========================================

def create_google_maps_link(location):

    if location is None:

        return None

    latitude = location["latitude"]
    longitude = location["longitude"]

    return (
        "https://www.google.com/maps/"
        f"search/?api=1&query="
        f"{latitude},{longitude}"
    )


# ==========================================
# GET GPS LOCATION
# ==========================================

def get_gps_location():

    """
    Placeholder for future GPS hardware.

    Later, GPS data from ESP32/GPS hardware
    will be received here.
    """

    print("\n🛰️ GPS")
    print("-----------------------------------")

    print(
        "Waiting for GPS hardware..."
    )

    return None