import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound


def speak(text):
    tts = gTTS(text=text, tld='US', lang='en', slow=False)
    filename = ('voice.mp3')
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		
		audio = r.listen(source)

		said = ""

		try:
		    said = r.recognize_google(audio)
		    print(said)
		except Exception as e:
		    print("Exception: " + str(e))

	return said

text = get_audio()

if "hello" in text:
    speak("hello, how are you?")
elif "what is your name" in text:
    speak("My name is Tim")



