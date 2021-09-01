import speech_recognition as sr
from playsound import playsound
import os
import inspect
currentpath = os.path.dirname(os.path.abspath(inspect.stack()[0][1])) 

def speechtotext():
    current_path = os.getcwd()
    r = sr.Recognizer()
    print(current_path)
    with sr.Microphone() as source:
        print("Listening....")
        r.adjust_for_ambient_noise(source,duration = 0.5)
        playsound(os.path.join(currentpath,"audio/opening.wav"))
        r.pause_threshold = 1
        # need an effective method here
        #audio = r.listen(source, timeout=7)
        audio = r.record(source,duration=10)
    try:
        print("Recognizing....")
        playsound(os.path.join(currentpath,"audio/closing.wav"))
        quary = r.recognize_google(audio, language='en-in')
        print("said:"+quary+"\n")
    except Exception as e:
        print(e)
        print("Say that again please....")
        q = speechtotext()
        quary = q
    return quary

