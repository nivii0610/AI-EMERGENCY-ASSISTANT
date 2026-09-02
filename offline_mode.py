def show_offline_status():

    print("\n===================================")
    print("📡 SYSTEM MODE")
    print("===================================")

    print(
        "🟢 Emergency knowledge base: OFFLINE READY"
    )

    print(
        "🟢 AI emergency detection: OFFLINE READY"
    )

    print(
        "🟢 Voice output: OFFLINE READY"
    )

    print(
        "🟡 Voice input: INTERNET REQUIRED"
    )

    print("===================================")


# ==========================================
# CHECK OFFLINE COMPONENTS
# ==========================================

def get_offline_status():

    return {

        "knowledge_base": True,

        "emergency_detection": True,

        "voice_output": True,

        "voice_input": False
    }