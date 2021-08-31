import keyboard
import setproctitle

import subprocess
import os

def get_pid(name):
    return subprocess.check_output(["pidof",name])
try:
    for i in get_pid('f8press').decode("utf-8").split():
        print("Killing")
        os.system("kill "+str(i))
except:
    pass
setproctitle.setproctitle('f8press')
while True:
    try:
        get_pid('Veronica')
    except:
        break
    if keyboard.read_key() == "f8":
        print("success")
        with open("keypress.txt","w") as f:
           f.write("True")
