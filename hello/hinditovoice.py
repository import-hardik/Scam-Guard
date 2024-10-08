from gtts import gTTS
import os

def hindi_text_to_speech_gtts(hindi_text):
    # Create a gTTS object for Hindi text
    tts = gTTS(text=hindi_text, lang='hi', slow=False)

    # Save the speech to a file
    tts.save("hindi_speech.mp3")

    # Play the speech
    os.system("start hindi_speech.mp3")  # This will play the saved MP3 file

# Example usage
if __name__ == "__main__":
    hindi_text = "नमस्ते, आप कैसे हैं?"
    hindi_text_to_speech_gtts(hindi_text)
