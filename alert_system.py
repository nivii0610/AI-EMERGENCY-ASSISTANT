from datetime import datetime


# ==========================================
# GENERATE EMERGENCY ALERT
# ==========================================

def generate_alert(
    emergency,
    severity,
    user_input,
    location
):

    current_time = datetime.now()

    time = current_time.strftime(
        "%Y-%m-%d %H:%M:%S"
    )


    # ==========================================
    # DISPLAY ALERT
    # ==========================================

    print("\n===================================")
    print("🚨 EMERGENCY ALERT")
    print("===================================")

    print("Time:", time)
    print("Emergency:", emergency)
    print("Severity:", severity)
    print("Description:", user_input)
    print("Location:", location)


    # ==========================================
    # SEVERITY MESSAGE
    # ==========================================

    if severity == "CRITICAL":

        print("\n🔴 CRITICAL EMERGENCY")

        print(
            "Immediate professional assistance "
            "may be required."
        )

    elif severity == "HIGH":

        print("\n🟠 HIGH-RISK EMERGENCY")

        print(
            "Follow emergency safety guidance "
            "and seek appropriate assistance."
        )

    elif severity == "MEDIUM":

        print("\n🟡 MEDIUM-RISK EMERGENCY")

        print(
            "Follow the recommended safety instructions "
            "and monitor the situation."
        )

    else:

        print("\n🟢 LOW-RISK EMERGENCY")

        print(
            "Follow the provided safety guidance."
        )


    print("===================================")


    # ==========================================
    # RETURN ALERT DATA
    # ==========================================

    return {

        "time": time,

        "emergency": emergency,

        "severity": severity,

        "description": user_input,

        "location": location
    }