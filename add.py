import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:

   engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()