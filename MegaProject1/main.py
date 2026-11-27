
import speech_recognition as sr
import pyttsx3
import webbrowser

recognizer = sr.Recognizer()
recognizer.dynamic_energy_threshold = True
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower:
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower:
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower:
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower:
        webbrowser.open("https://linkedin.com")
    else:
        speak("Sorry can't help you with this.")
        
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