
import speech_recognition as sr
import pyttsx3
import webbrowser

recognizer = sr.Recognizer()
recognizer.dynamic_energy_threshold = True
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            except sr.WaitTimeoutError:
                print("No speech detected.")
                continue

        try:
            text = recognizer.recognize_google(audio)
            if(text.lower() == "jarvis"):
                print("yes")
            else:
                print(f"You said: {text}")
        except sr.UnknownValueError:
            print("Sorry, could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from the service; {e}")