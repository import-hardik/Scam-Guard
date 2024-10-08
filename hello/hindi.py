import os
import google.generativeai as genai
import speech_recognition as sr
import sys
from gtts import gTTS

def hindi_text_to_speech_gtts(hindi_text):
    # Create a gTTS object for Hindi text
    tts = gTTS(text=hindi_text, lang='hi', slow=False)

    # Save the speech to a file
    tts.save("hindi_speech.mp3")

    # Play the speech
    os.system("start hindi_speech.mp3")  # This will play the saved MP3 file

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


genai.configure(api_key="AIzaSyB3mI8isXKm1TWQSOjU-hsdEXxv8I5n4nk")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
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
      "role": "model",
      "parts": [
        "**This is a scam.**  \n\nHere's why:\n\n* **Urgency:** The message uses a sense of urgency and fear (\"your child doing bad things,\" \"go to jail\") to pressure you into acting quickly.\n* **Lack of Official Contact:**  Legitimate law enforcement officers would never contact you through informal channels like this. They would have a formal process involving direct contact, official documentation, and potential court involvement.\n* **Requesting Money:** Law enforcement officers do not ask for money to release someone from custody. \n* **Grammatical Errors:** The message contains grammatical errors, which is another red flag of a scam.\n\n**What to do:**\n\n* **Do not respond.**\n* **Report the message:**  You can report the message to the platform where you received it (e.g., email provider, social media platform) and to the appropriate authorities (e.g., local police, FBI).\n* **Contact your child:** If you are genuinely concerned about your child, contact them directly to ensure they are safe.\n\n**Remember:**  Scammers often use emotional manipulation to trick people into giving them money or personal information. If something feels off, it likely is. \n",
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

recognized_text = speech_to_text()
print("User :",recognized_text)
if recognized_text:
    textyou=recognized_text
    response = chat_session.send_message(textyou)

print(response.text)
hindi_text_to_speech_gtts(response.text)