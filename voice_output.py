import pyttsx3


# ==========================================
# CREATE VOICE ENGINE
# ==========================================

engine = pyttsx3.init()


# ==========================================
# VOICE SETTINGS
# ==========================================

# Speaking speed
engine.setProperty("rate", 165)

# Volume: 0.0 to 1.0
engine.setProperty("volume", 1.0)


# ==========================================
# SPEAK FUNCTION
# ==========================================

def speak(text):

    # Also display the message in terminal
    print("\n🔊 Assistant:")
    print(text)

    # Speak the message
    engine.say(text)
    engine.runAndWait()

