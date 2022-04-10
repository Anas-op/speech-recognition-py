import speech_recognition
from neuralintents import GenericAssistant
import pyttsx3 as tts
import sys
import random

recognizer = speech_recognition.Recognizer()  # set recognizer object

speaker = tts.init()  # init object

speaker.setProperty('rate', 150)  # set rate for the speaker, fast or low 20 or 300



# assistant.request("How are you")   # going to look in dialogue and finds the corresponding request "How are you"


def create_note():
    global recognizer

    speaker.say("What do you want to write?")
    speaker.runAndWait()
    done = False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.8)
                audio = recognizer.listen(mic)
                note = recognizer.recognize_google(audio, language="en-GB")  # recognize text of audio
                note = note.lower()
                speaker.say("Choose a filename!")
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic, duration=0.8)
                audio = recognizer.listen(mic)
                filename = recognizer.recognize_google(audio)
                filename = filename.lower()
            with open(filename, 'w') as f:
                f.write(note)
                done = True
                speaker.say("successfully created the note")
                speaker.runAndWait()
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand")
            speaker.runAndWait()


def Hello():
    global recognizer
    speaker.say("What do you want to write?")
    speaker.runAndWait()
    done = False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                note = recognizer.recognize_google(audio,  language="en-GB")  # recognize text of audio
                note = note.lower()
                speaker.say("Choose a filename!")
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                filename = recognizer.recognize_google(audio,  language="en-GB")
                filename = filename.lower()
            with open(filename, 'w') as f:
                f.write(note)
                done = True
                speaker.say("successfully created the note")
                speaker.runAndWait()
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand")
            speaker.runAndWait()

def GoodBye():
    speaker.say("Goodbye")
    sys.exit(0)


# creating a mappings dictionary

mappings = {
    "greeting": Hello,
    "goodbye": GoodBye
}

assistant = GenericAssistant("intents.json",
                             intent_methods=mappings)  # sets the file from which it will retrieve intents
assistant.train_model()  # we train the model after specifying the file.json

# connect a function to request of the model
# mappings = {'greeting': function}  # if we recognize the function of tag greeting then it will execute the function
# assistant = GenericAssistant('dialogue.json', intent_methods=mappings)   # assigning the mapping to the model assistant
# assistant.train_model()


while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, 1)
            audio = recognizer.listen(mic)

            message = recognizer.recognize_google(audio,  language="en-GB")
            message = message.lower()
        assistant.request(message)
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
        speaker.say("I did not understand")
        speaker.runAndWait()
