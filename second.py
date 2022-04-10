import speech_recognition as sr
from neuralintents import GenericAssistant
import pyttsx3 as tts
import sys
import json
import random


speaker = tts.init()  # init object
speaker.setProperty('rate', 150)
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)
recording = sr.Recognizer()
message = []
w = ''


def GoodBye():
    global message, w
    with open("intents.json") as file:
        data = json.load(file)
        for intent in data["intents"]:
            for pattern in intent["patterns"]:
                if message in str(intent["patterns"]).lower():
                    w = intent["responses"]
    speaker.say(random.choice(w))
    speaker.runAndWait()
    sys.exit(0)

def Greeting():
    global message, w
    with open("intents.json") as file:
        data = json.load(file)
        for intent in data["intents"]:
            for pattern in intent["patterns"]:
                if message in str(intent["patterns"]).lower():
                    w = intent["responses"]
    speaker.say(random.choice(w))
    speaker.runAndWait()


def Thanking():
    global message, w
    with open("intents.json") as file:
        data = json.load(file)
        for intent in data["intents"]:
            for pattern in intent["patterns"]:
                if message in str(intent["patterns"]).lower():
                    w = intent["responses"]
    speaker.say(random.choice(w))
    speaker.runAndWait()







mappings = {
    "goodbye": GoodBye,
    "greeting": Greeting
}

assistant = GenericAssistant("intents.json",
                             intent_methods=mappings)  # sets the file from which it will retrieve intents
assistant.train_model()  # we train the model after specifying the file.json



while True:
    with sr.Microphone() as source:
        recording.adjust_for_ambient_noise(source)
        print("Please Say something")
        speaker.runAndWait()
        audio = recording.listen(source)

    try:
        message = recording.recognize_google(audio)
        message = message.lower()
        assistant.request(message)
        #print("You said: " + message)

    except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            speaker.say("I did not understand")
            speaker.runAndWait()




