import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")    
    elif hour>=12 and hour<18:
        speak('Good Afternoon!')
    else:
        speak('good evening!')

    speak(' I am jarvis my lord . how can i help u')    

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening sir.. .. .')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('recognizing.. .. .. .')     
        query = r.recognize_google(audio,language='en-in')
        print(f"user said : {query}\n")

    except Exception as e:
       # print(e)

        speak('Say again..... my lord')
        return "None"
    return query

if __name__ =="__main__":
    wishMe()  
    
   #while (True):
    if 2:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences = 3)
            speak('According to wikipedia')
            print(results)
            speak(results)
        elif 'open YouTube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open code' in query:
            codePath = "C:\\Users\\bhuva\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime( "%H:%M:%S")
            speak(f"Sir, the time is{strTime}")






