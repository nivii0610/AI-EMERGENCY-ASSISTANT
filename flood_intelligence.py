# flood_intelligence.py


def assess_flood_risk(
    water_level_feet,
    current_floor,
    total_floors,
    evacuation_available=True
):
    """
    Estimate flood risk and provide safety guidance.

    NOTE:
    This is a prototype decision-support system.
    It does NOT guarantee that a particular floor is safe.
    """

    try:
        water_level_feet = float(water_level_feet)
        current_floor = int(current_floor)
        total_floors = int(total_floors)

    except ValueError:

        return {
            "risk": "UNKNOWN",
            "message": "Invalid flood or building information.",
            "recommendation": "Follow official emergency instructions."
        }

    # Basic validation
    if water_level_feet < 0:
        return {
            "risk": "UNKNOWN",
            "message": "Water level cannot be negative.",
            "recommendation": "Check the sensor or entered information."
        }

    if current_floor < 0 or total_floors <= 0:
        return {
            "risk": "UNKNOWN",
            "message": "Invalid building information.",
            "recommendation": "Check the building details."
        }

    if current_floor > total_floors:
        return {
            "risk": "UNKNOWN",
            "message": "Current floor cannot be above the total number of floors.",
            "recommendation": "Check the building details."
        }

    # Determine basic risk from water level
    if water_level_feet < 1:
        risk = "LOW"

    elif water_level_feet < 3:
        risk = "MEDIUM"

    elif water_level_feet < 5:
        risk = "HIGH"

    else:
        risk = "CRITICAL"

    # Build recommendation
    if evacuation_available:

        recommendation = (
            "Follow official evacuation instructions and move to "
            "a designated safe location if instructed."
        )

    else:

        recommendation = (
            "If evacuation is not possible, move toward a safer "
            "elevated location and stay away from floodwater."
        )

    # Add building information
    if current_floor < total_floors:

        building_message = (
            f"You are currently on floor {current_floor} "
            f"of a {total_floors}-floor building. "
            "A higher floor may provide greater elevation, "
            "but the system cannot guarantee that any floor is safe."
        )

    else:

        building_message = (
            "You are currently on the highest reported floor. "
            "Continue following official emergency instructions."
        )

    # Important flood warnings
    warnings = [
        "Do not walk or drive through moving floodwater.",
        "Avoid contact with electrical equipment or outlets in flooded areas.",
        "Do not use elevators if flooding or power failure is possible.",
        "Follow instructions from local emergency authorities."
    ]

    return {
        "risk": risk,
        "water_level": water_level_feet,
        "current_floor": current_floor,
        "total_floors": total_floors,
        "message": building_message,
        "recommendation": recommendation,
        "warnings": warnings
    }


def display_flood_assessment(result):

    print("\n🌊 FLOOD SAFETY ASSESSMENT")
    print("===================================")

    print("Flood Risk:", result["risk"])
    print("Water Level:", result["water_level"], "feet")

    print("\n🏢 Building Information:")
    print(
        "Current Floor:",
        result["current_floor"]
    )

    print(
        "Total Floors:",
        result["total_floors"]
    )

    print("\n📍 Assessment:")
    print(result["message"])

    print("\n⚠️ Recommendation:")
    print(result["recommendation"])

    print("\n🚨 Important Safety Warnings:")

    for warning in result["warnings"]:
        print("→", warning)