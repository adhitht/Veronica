import os
import inspect
import shutil
import subprocess
currentpath = os.path.dirname(os.path.abspath(inspect.stack()[0][1])) 

print("Installing dependencies for pyaudio")
os.system("sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0")
os.system("sudo apt-get install ffmpeg")

os.system("sudo apt-get install libatlas-base-dev libmagic-dev")

print("installing sox and pyaudio")
os.system("sudo apt-get install sox python3-pyaudio")

print("Initialising Snowboy")
subprocess.Popen(["make"], stdout=subprocess.PIPE, cwd=currentpath+"/snowboy/swig/Python3")

shutil.copy2(os.path.join(currentpath,"snowboy/swig/Python3/_snowboydetect.so"), currentpath)
shutil.copy2(os.path.join(currentpath,"snowboy/swig/Python3/snowboydetect.py"), currentpath)

os.system("pip3 install -r requirements.txt")

print('''Veronica is now ready to be used
Before that make sure that you have obtained pmdl file from docker and had pasted in \"models\" folder.''')
from tts import veronicatts
try:
  veronicatts("Hello, Good to see you")
except:
  print("There's some problem")
