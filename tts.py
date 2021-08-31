from gtts import gTTS
from playsound import playsound
import os
import inspect
def veronicatts(speech_text):
    currentpath = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
    tts = gTTS(speech_text,slow=False)
    tts.save(currentpath+'/tts.mp3')
    playsound(currentpath+"/tts.mp3")

