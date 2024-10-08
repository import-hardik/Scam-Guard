import speech_recognition as sr
import sys

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")

        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=1)

        # Listen for audio
        try:
            audio = recognizer.listen(source, timeout=4)
            print("Audio recorded successfully. Recognizing...")

            # Use Google Web Speech API for recognition
            recognized_text = recognizer.recognize_google(audio,language="hi-IN")
            sys.stdout.reconfigure(encoding='utf-8')
            return recognized_text

        except sr.WaitTimeoutError:
            print("No speech detected")
            return ""

        except sr.RequestError as e:
            print("Could not request results from Google Web Speech API; {0}".format(e))
            return ""

        except sr.UnknownValueError:
            print("Google Web Speech API could not understand audio")
            return ""


recognized_text = speech_to_text()
if recognized_text:
    print("Recognized Text:", recognized_text)


