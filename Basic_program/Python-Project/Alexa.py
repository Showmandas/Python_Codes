import speech_recognition as spr
import pyttsx3
import datetime

listener=spr.Recognizer()
alexa=pyttsx3.init()
voices=alexa.getProperty('voices')
alexa.setProperty('voice',voices[1].id)

def talk(text):
    alexa.say()
    alexa.runAndWait()

def take_cmd():
    
    try:
        with spr.Microphone() as audio:
            print('Listening...')
            voice=listener.listen(audio)
            cmd=listener.recognize_google(voice)
            cmd=cmd.lower()
            if 'alexa' in cmd:
                print(cmd)

    except:
        pass

    return cmd

def run_alexa():
    command=take_cmd()
    if 'time' in    command:
        time=datetime.datetime.now().strftime()
        talk(time)