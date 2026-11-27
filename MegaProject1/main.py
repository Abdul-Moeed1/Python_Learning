
import speech_recognition as sr
import pyttsx3
import webbrowser
import os
from dotenv import load_dotenv
import requests
from openai import OpenAI

# Loads variables from .env into the system environment
load_dotenv()

recognizer = sr.Recognizer()
recognizer.dynamic_energy_threshold = True
engine = pyttsx3.init()
newsApiKey = os.getenv("NEWS_API_KEY")
groqApiKey = os.getenv("GROQ_API_KEY")

client = OpenAI(
    api_key=groqApiKey,
    base_url="https://api.groq.com/openai/v1"
)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=sa&apiKey={newsApiKey}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles" , [])
            for article in articles:
                speak(article)
    else:
        # Let OpenAI handle the request .
        generateAIResponse(c)

def generateAIResponse(c):
    response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    max_tokens=150,  # Hard limit on output tokens
    messages=[
        {"role": "system", "content": "Reply in 1 or 2 short sentences only."},
        {"role": "user", "content": c}
    ]
    )
    speak(response.choices[0].message.content)
        
if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            try:
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
            except sr.WaitTimeoutError:
                print("No speech detected.")
                continue

        try:
            word = recognizer.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("ya")
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    print("Jarvis Active...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)

                           
                
            else:
                print(f"You said: {word}")
        except sr.UnknownValueError:
            print("Sorry, could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from the service; {e}")