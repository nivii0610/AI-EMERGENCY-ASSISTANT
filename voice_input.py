import speech_recognition as sr


def get_voice_input(prompt="Speak now."):

    recognizer = sr.Recognizer()

    print("\n🎤 VOICE INPUT")
    print("-----------------------------------")
    print(prompt)

    try:

        with sr.Microphone() as source:

            print("🎧 Listening...")

            # Reduce background-noise effect
            recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=15
            )

        print("🧠 Processing your voice...")

        text = recognizer.recognize_google(audio)

        print("\n📝 You said:")
        print(text)

        return text

    except sr.WaitTimeoutError:

        print("\n❌ No speech detected.")
        return ""

    except sr.UnknownValueError:

        print("\n❌ I couldn't understand what you said.")
        return ""

    except sr.RequestError:

        print("\n❌ Speech recognition service is unavailable.")
        return ""

    except Exception as error:

        print("\n❌ Voice input error:", error)
        return ""