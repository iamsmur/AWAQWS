import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
from tkinter import *
from tkinter import messagebox

#from weather import Weather, Unit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    engine.setProperty('rate', 135)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Friday Sir. Please tell me how may I help you")

    return 0



'''def takeCommand():
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
        print("Say that again please...")  
        return "None"
    return query'''


'''def takeCommand():

    
    r = input("Enter Query:\n") t

    try:
        # print("Recognizing...")
        #print("searching..")
        # query = r.recognize_google(audio, language='en-in')

        print(f"User said: {r}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return r'''


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()




def friday():
        # if 1:
        query = takeCommand().lower()

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
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'D:\A Qawwali'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[3]))

        elif 'the time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"Sir, the time is {strTime}")


        elif 'open code' in query:
            codePath = ""
            os.startfile(codePath)
        elif 'who are you' in query:
            speak("Sir, I'm Friday a lovely virtual assistant")

        elif 'love sex girlfriend' in query:
            speak("'I think it's awesome")

        elif 'are you doing' in query:
            speak("Sir, I'am in process!")
        # elif '' in query:
         #   speak("Sir, Enter a valid Details.I can't understand what are you trying")
        elif 'exit' in query:
            exit()


if __name__ == "__main__":

    window = Tk()

    window.title("Friady App")

    window.geometry('350x200')

    btn = Button(window,text="Start", bg="yellow", command=wishMe)
    btn.grid(column=1, row=0)

    txt = Entry(window, width=10)

    txt.grid(column=1, row=1)

    def takeCommand():

        r = txt.get()

        try:
            print(f"User said: {r}\n")


        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"

        return r


    #btn2 = Button(window, text="Query", bg="orange", command=takeCommand())
    #btn2.grid(column=1, row=4)

    btn3 = Button(window, text="friday", bg="red", command=friday)
    btn3.grid(column=1, row=3)

    window.mainloop()

