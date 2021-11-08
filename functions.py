from imports import *

def list_to_string(s): 
    str1 = ""   
    for elem in s: 
        str1 += elem  
    return str1 

#NO.0 Greet
def greet():
    greet = ["I am fine","Fine here","How are you","Fine"]
    random_greet  = random.choice(greet)
    veronicatts(random_greet)

#NO.1  Google Search
def searchforwebsite(txt):
    words_to_be_removed = ["search","for","website","site"]
    txtlist = txt.split()
    for i in words_to_be_removed:
        if i in txtlist:
            txtlist.remove(i)
    search_query = list_to_string(txtlist)
    search_list = []
    for j in search(search_query,num_results=2):
        search_list.append(j)
    veronicatts("Opening Website")
    if len(search_list) !=0:
        webbrowser.open(search_list[0])

#NO.2
def take_screenshot():
    subprocess.Popen("gnome-screenshot")
#No.3
def get_time():
    now = datetime.now()
    current_time = now.strftime("%-I %-M %p")
    veronicatts(f"It's {current_time} now")
#NO.4
def lock_my_pc():
    subprocess.Popen("gnome-screensaver-command -l".split())

def didntfetch():
    veronicatts("Sorry, Couldn't get that")