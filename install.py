import os
import inspect
import shutil

currentpath = os.path.dirname(os.path.abspath(inspect.stack()[0][1])) 

print("Installing dependencies for pyaudio")
os.system("sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0")
os.system("sudo apt-get install ffmpeg")

os.system("sudo apt-get install libatlas-base-dev libmagic-dev")

print("installing sox and pyaudio")
os.system("sudo apt-get install sox python3-pyaudio")

print("Now open terminal and go to "+currentpath+"/snowboy/swig/Python3 (using cd or going to path in nautilus and opening with terminal). type \"make\" in terminal.")
kk = input("Press Enter if you have done that. (Now or Earlier)")

shutil.copy2(os.path.join(currentpath,"snowboy/swig/Python3/_snowboydetect.so"), currentpath)
shutil.copy2(os.path.join(currentpath,"snowboy/swig/Python3/snowboydetect.py"), currentpath)

os.system("pip3 install -r requirements.txt")