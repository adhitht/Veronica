import subprocess
from fuzzywuzzy import process
cmd = ['whoami']
whoami = subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0]
def get_app(app_name):
    cmdd = "ls /usr/share/applications | awk -F '.desktop' ' { print $1}' -"
    output = subprocess.Popen(cmdd, shell = True,stdout=subprocess.PIPE ).communicate()[0]
    outputstr = output.decode('UTF-8')
    outputlist= outputstr.split("\n")
    outputlist.append("telegram-desktop")
    websites_open = [
        "https://www.google.com",
        "https://gmail.com",
        "https://www.facebook.com",
        "https://www.youtube.com",
        "https://www.amazon.com",
        "https://www.flipkart.com",
        "https://www.wikipedia.com",
        "https://web.whatsapp.com",
        "https://www.instagram.com",
        "https://www.unacademy.com"
    ]
    system_files = [
        "/home/"+whoami[:-1].decode("utf-8")+"/Downloads",
        "/home/"+whoami[:-1].decode("utf-8")+"/Music",
        "/home/"+whoami[:-1].decode("utf-8")+"/Documents",
        "/home/"+whoami[:-1].decode("utf-8")+"/Desktop",
        "/home/"+whoami[:-1].decode("utf-8")+"/Pictures",
        "/home/"+whoami[:-1].decode("utf-8")+"/Videos",
    ]
    outputlist += websites_open
    outputlist += system_files
    name,percent = process.extractOne(app_name,outputlist)
    return name,percent
