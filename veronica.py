from importsmain import *

currentpath = os.path.dirname(os.path.abspath(inspect.stack()[0][1])) 
logfilepath = os.path.join(currentpath,"logs/log.txt")
errorfilepath = os.path.join(currentpath,"logs/error.txt")

#NOTE THESE FILES ARE NOT SEND TO ANYWHERE. LOG AND ERROR FILES STAYS
# ON YOUR COMPUTER UNLESS YOU SEND IT. THESE FILES ARE HELPFUL TO RESOLVE 
# ANY ERRORS

def checkandcreatefile(x,y):
    if os.path.exists(x) == False:
        if ".txt" in x:
            with open(x,"w+") as f:
                f.write(y)
        else:
            os.mkdir(x)

#Checking if log files are present if not creating
checkandcreatefile(os.path.join(currentpath,"logs"), "asdad")
checkandcreatefile(logfilepath,"Log File created at "+datetime.now().strftime("%d %b %Y %I:%M:%S %p"))
checkandcreatefile(errorfilepath,"Error File created at "+datetime.now().strftime("%d %b %Y %I:%M:%S %p"))
checkandcreatefile(os.path.join(currentpath,"keypress.txt"),"False")

def errorrlog(*text):
    global errorfilepath
    with open(errorfilepath,"a+") as errorfile:
        for i in text:
            errorfile.write(i)

def logging(*text):
    global logfilepath
    with open(logfilepath,"a+") as logfile:
        for i in text:
            logfile.write(i)

#LOGGING DETAILS SUCH AS START TIME,TIME ZONE,....
with open(logfilepath,"a+") as logfile:
    logging("\n\nStart Time: ",
    datetime.now().strftime("%d %b %Y %I:%M:%S %p").rjust(24),
    "\n",
    "DISTRIBUTION: "+str(distro.linux_distribution()))

def get_pid(name):
    return subprocess.check_output(["pidof",name])

try:
    count = 0
    for i in get_pid('Veronica').decode("utf-8").split():
        count += 1
    if count == 1:
        veronicatts("Found a running instance of Veronica. Please close")
    elif count > 1:
        veronicatts("Found multiple running instances of Veronica. Please close them")
except:
    pass

with open("keypress.txt","w+") as f:
    f.write("False")

setproctitle.setproctitle('Veronica')
print("Initialised")
playsound(currentpath+"/audio/start.mp3")

manoeuvre = False

def commands_func(txt):
    command_one = getcommand(txt) 
    global logfilepath
    with open(logfilepath,"a+") as logfile:
        logging("\n"," "*28+"Result: "+str(command_one),"\n")
    if command_one != None:
        command_name = command_one[0]
        print(command_name)
        command_result = eval(command_name)
        command_thread = threading.Thread(target=command_result, args=(1,))
        command_thread.start()

def keypress():
    path_for_f8 = os.path.join(currentpath,"f8press.py")
    os.system("sudo -A python3 "+path_for_f8)

def keypress_detect():
    while True:
        with open("keypress.txt","r") as file:
            if file.readline() == "True":
                after_detection()

def detector_snowboy():
    modelspath = os.path.join(currentpath,"models/")
    try:
        detector = snowboydecoder.HotwordDetector(modelspath+"veronica.pmdl", sensitivity=0.45, audio_gain=3)
    except Exception as e:
        print(e)
        print("Hotword Engine Not Running")
        errorrlog("Hotword Problem","\n",e)
    global manoeuvre
    manoeuvre = True
    detector.start(after_detection)

def after_detection():
    speech_text = speechtotext()
    global logfilepath
    with open(logfilepath,"a+") as logfile:
        logging("\n",datetime.now().strftime("%d %b %Y %I:%M:%S %p").rjust(24),"--> Query: "+str(speech_text))

    if "open" in speech_text:
        app_name,app_percent = get_app(speech_text.replace("open",""))
        print(app_name,app_percent)
        if app_percent > 80:
            print(app_name)
            try:
                if "https" in app_name or "/home" in app_name:
                    app_name = "xdg-open "+app_name
                subprocess.Popen(app_name.split())
                logging("\n"," "*28+"Result: "+"Opened "+str(app_name),"\n")
            except Exception as e:
                errorfilepath("Error in opening "+app_name)
                print("Some error occured in opening app. If found please report at https://github.com/adhitht123/Veronica. ")
                print(e)
        else:
            commands_func(speech_text)
    else:
        commands_func(speech_text)
    global manoeuvre
    manoeuvre = False
    with open("keypress.txt","w+") as f:
        f.write("False")

keypress_thread = threading.Thread(target=keypress)
keypress_thread.start()
keypress_detect_thread = threading.Thread(target=keypress_detect)
keypress_detect_thread.start()
detector_thread = threading.Thread(target=detector_snowboy(), args=(1,))
detector_thread.start()