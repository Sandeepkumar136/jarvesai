import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Your Rita, sir. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language="en-in")
        print('User Said:', query)
    except Exception as e:
        print("Say that again, please...")
        return "None"
    return query
if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)
        elif 'open youtube' in query:
            speak("Opening YouTube...")
            webbrowser.open('https://www.youtube.com/')
        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open('https://www.google.co.in/')
        elif 'open github' in query:
            speak("Opening GitHub...")
            webbrowser.open('https://github.com/')
        elif 'open stack overflow' in query:
            speak("Opening Stack Overflow...")
            webbrowser.open('https://stackoverflow.com/')
        elif 'play music' in query:
            speak("Playing music...")
            music_dir = "D:\Music"  # Provide the correct path
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("The time is " + strtime)
        elif 'open code' in query:
            codepath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code Insiders\\Code - Insiders.exe"
            os.startfile(codepath)
        elif 'open toolbox' in query:
            toolpath = "C:\\Users\\DELL\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe"
            os.startfile(toolpath)