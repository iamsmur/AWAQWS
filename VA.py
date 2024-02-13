from random import random

import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
from tkinter import *

from weather import Weather, Unit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    engine.setProperty('rate', 132)



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Sir, I am Zaarah Please tell me how may I help you")

    while True:
        # if 1:
        query = takeCommand().lower()
        lbl.grid(column=5, row=6)
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            ok()
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play a song' in query:
            ok()
            music_dir = 'D:\A Qawwali'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[3]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'weather' in query:
            weather = Weather(unit=Unit.CELSIUS)
            lookup = weather.lookup(560743)
            condition = lookup.condition
            speak(f"Sir, weather {condition}")

        elif 'open' in query:
            speak('which Application want to start')

            codePath = takeCommand()

            try:

                os.startfile(codePath)


            except Exception as e:
                # print(e)
                speak("I can't understand please Say only application name ")





        elif 'stop' in query:
            speak('which Application want to stop')
            killapp = takeCommand()
            os.system(f"taskkill /f /im {killapp}.exe")
            speak('Not listed application')
        elif 'who are you' in query:
            speak("Sir, I'm Zaarah a lovely virtual assistant")

        elif 'stop music' in query:
            os.system("taskkill /f /im vlc.exe")

        elif 'are you doing' in query:
            speak("Sir, I'am in process!")

        elif 'band ho jao' in query:
            ok()
            exit()



def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please..")
        speak("I can't understand Say that again please..")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def ok():
    speak('ok sir')
    return 0


if __name__ == "__main__":

    window = Tk()

    window.title("Welcome to Zaarah")

    window.geometry('350x200')

    lbl = Label(window, text="Zaarah")

    lbl.grid(column=3, row=0)

    btn = Button(window, text="Start", bg="red", command=wishMe)
    btn.grid(column=5, row=5)

    window.mainloop()





