import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia#pip install wikipedia
import webbrowser
import os
import cv2,time
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am JARVIS Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
        print("OK")

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print("User said:"+query)

    except sr.UnknownValueError:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand()

        # Logic for executing tasks based on query
        if 'Wikipedia' in query:
            speak("ok")
            speak('What am i searching for...')
            query = takeCommand()
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open stackoverflow' in query:
            speak("ok")
            webbrowser.open("www.stackoverflow.com")


        elif 'play video' in query:
            speak("ok")
            music_dir = 'C:\\Users\\subha\\Videos\\MOVIES'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            speak("ok")
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'play songs' in query:
            speak("ok")
            music_dir=("C:\\Users\\subha\\Music\\songs")
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'search' in query:
            speak("ok")
            speak('What am i searching for...')
            query = takeCommand()
            open="https://www.google.com/search?q="+query
            webbrowser.open(open)

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'what is your name' in query:
            speak("My name is JARVIS")

        elif 'weather' in query:
            speak("Weather of which city")
            query1 = takeCommand()
            webbrowser.open("https://openweathermap.org/find?q="+query1)

        elif 'capture image' in query:
            i=0
            speak("capturing image")
            video=cv2.VideoCapture(0)
            while(i<1):
                check,frame=video.read()
                cv2.imwrite('C:\\Users\\subha\\Pictures\\img1.jpg',frame)
                cv2.imshow("capturing",frame)
                cv2.waitKey(10000)
                i+=1
            video.release()
            cv2.destroyAllWindows()
