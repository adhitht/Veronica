from fuzzywuzzy import process
from playsound import playsound
#DEMO
'''
1:{"commands":[],"func":""},
'''
command_dict={
    0:{"commands":["hai","hello","how are you"], "func":"greet"},
    1:{"commands":["search for website","search for site"],"func":"searchforwebsite"},
    2:{"commands":["take screenshot","screenshot"], "func":"take_screenshot"},
    3:{"commands":["whats the time","time like"],"func":"get_time"},
    4:{"commands":["lock my pc","lock computer","lock pc"],"func":"lock_my_pc"}
}
special_commands = ["searchforwebsite"]

def getcommand(txt):
    match_percent = 0
    for key in command_dict:
        details,percent = process.extractOne(txt, command_dict[key]["commands"])
        print(details,percent)
        if percent > match_percent:
            match_percent = percent
            command = command_dict[key]["func"]
            finaldetail = details
    if match_percent > 85:
        if command in special_commands:
            command = command+"(\"{tx}\")".format(tx=txt)
        else:
            command = command+"()"
        return command, finaldetail
    else:
        return None
