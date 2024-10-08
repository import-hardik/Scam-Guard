import pyttsx3

def hindi_text_to_speech(hindi_text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set the properties (optional)
    engine.setProperty('rate', 150)    # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

    # Set the voice to a Hindi-speaking voice (if available)
    voices = engine.getProperty('voices')
    
    # Loop through available voices and find Hindi (based on voice name or id)
    for voice in voices:
        if 'hindi' in voice.name.lower():  # Check if the voice supports Hindi
            engine.setProperty('voice', voice.id)
            break

    # Say the Hindi text
    engine.say(hindi_text)

    # Process and run the speech command
    engine.runAndWait()

# Example usage
if __name__ == "__main__":
    hindi_text = "Scam"
    hindi_text_to_speech(hindi_text)