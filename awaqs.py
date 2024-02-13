import datetime
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
print("Chhaaya is Ready..")
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    engine.setProperty('rate', 145)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<17:
        speak("Good Afternoon!")

    elif hour>17 and hour<19:
        speak("Good Evening!")

    else:
        speak("Good Night!")

    speak("I am Chhaaya Sir, Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)

        print("Say That again please...")
        return "None"
    return r
    '''

def takeCommand():
    #It takes microphone input from the user and returns string output
    r= input("Enter Query:\n")


    try:
        #print("Recognizing...")
        print("searching..")
        #query = r.recognize_google(audio, language='en-in')

        print(f"User said: {r}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return r'''


if __name__ == "__main__":
    speak(" ")
    wishMe()
    takeCommand()