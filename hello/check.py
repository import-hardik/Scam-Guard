import pyttsx3

def list_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    # Print available voices
    for voice in voices:
        print(f"Voice: {voice.name}, ID: {voice.id}, Language: {voice.languages}")

list_voices()