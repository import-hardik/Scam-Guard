import os
import google.generativeai as genai
import speech_recognition as sr
import sys
from gtts import gTTS
import pyttsx3

def hindi_text_to_speech_gtts(hindi_text):
    # Create a gTTS object for Hindi text
    tts = gTTS(text=hindi_text, lang='hi', slow=False)

    # Save the speech to a file
    tts.save("hindi_speech.mp3")

    # Play the speech
    os.system("start hindi_speech.mp3")  # This will play the saved MP3 file

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

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")

        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=1)

        # Listen for audio
        try:
            audio = recognizer.listen(source, timeout=None)
            print("Audio recorded successfully. Recognizing...")

            # Use Google Web Speech API for recognition
            #recognized_text = recognizer.recognize_google(audio,language="hi-IN")
            recognized_text = recognizer.recognize_google(audio)
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


genai.configure(api_key="")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 100,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="Act as a cybersecurity officer. Your task is to analyze the provided text and determine if it contains a scam. Reply with either 'Scam' or 'Not Scam.' Do not provide any explanations.",
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Hello i am pollice officer i have caught your child dooing bad things please send some money if you want him to not go to jail",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Hello i am pollice officer i have caught your child dooing bad things please send some money if you want him to not go to jail",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Scam \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "hello this is from gov do not share your data with anyone online",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Not scam \n",
      ],
    },
  ]
)
response=""
#recognized_text = "Hi Sarah,I hope you're doing well! I wanted to remind you about our meeting scheduled for this Thursday at 2 PM in the conference room. We'll be discussing the upcoming project deadlines and strategies for the next quarter. If you have any questions or need to reschedule, please let me know. Looking forward to seeing you!Best,John"#voice to text
#recognized_text = "Congratulations! You've been selected for an exclusive offer to receive a $1,000 gift card. All you need to do is click the link below and provide your personal information. This offer is valid for a limited time only, so don't miss out! Act now to secure your gift. Remember, your satisfaction is our top priority. If you have any questions, please reply to this email."#voice to text
recognized_text = speech_to_text()#voice to text
print("You Said: ",recognized_text)
if recognized_text:
    textyou=recognized_text
    response = chat_session.send_message(textyou)
if response =="":
    hindi_text_to_speech("speech not recognized")
print(response.text)
hindi_text_to_speech(response.text)
