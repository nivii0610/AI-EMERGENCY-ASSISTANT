def detect_emergency(user_input):

    text = user_input.lower()

    # Flood
    flood_words = [
        "flood",
        "flooded",
        "flooding",
        "water rising",
        "water entering",
        "underwater",
        "heavy water"
    ]

    # Fire
    fire_words = [
        "fire",
        "burning",
        "smoke",
        "flames",
        "building is burning"
    ]

    # Earthquake
    earthquake_words = [
        "earthquake",
        "earth quake",
        "ground shaking",
        "ground is shaking",
        "building shaking",
        "tremor"
    ]

    # Heatwave
    heatwave_words = [
        "heatwave",
        "heat wave",
        "extreme heat",
        "very hot",
        "too much heat",
        "temperature is very high"
    ]

    # Cyclone / Storm
    cyclone_words = [
        "cyclone",
        "storm",
        "strong winds",
        "heavy winds",
        "tropical storm"
    ]

    # Road accident
    accident_words = [
        "accident",
        "car crash",
        "road crash",
        "vehicle crash",
        "bike accident",
        "traffic accident"
    ]

    # Check categories

    if any(word in text for word in flood_words):
        return "FLOOD"

    elif any(word in text for word in fire_words):
        return "FIRE"

    elif any(word in text for word in earthquake_words):
        return "EARTHQUAKE"

    elif any(word in text for word in heatwave_words):
        return "HEATWAVE"

    elif any(word in text for word in cyclone_words):
        return "CYCLONE / STORM"

    elif any(word in text for word in accident_words):
        return "ROAD ACCIDENT"

    else:
        return "UNKNOWN"