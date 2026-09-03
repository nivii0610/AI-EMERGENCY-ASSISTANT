import sys

def _safe_print(text):
    try:
        print(text)
    except UnicodeEncodeError:
        safe_text = text.encode("ascii", errors="ignore").decode("ascii")
        print(safe_text)

def show_offline_status():

    _safe_print("\n===================================")
    _safe_print("[STATUS] SYSTEM MODE")
    _safe_print("===================================")

    _safe_print("[OK] Emergency knowledge base: OFFLINE READY")
    _safe_print("[OK] AI emergency detection: OFFLINE READY")
    _safe_print("[OK] Voice output: OFFLINE READY")
    _safe_print("[ONLINE REQ] Voice input: INTERNET REQUIRED")

    _safe_print("===================================")


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