# Veronica
Personal Assistant for Linux.

## Supports
Currently Linux (Ubutnu 20.04) is supported. 
You may check if other distros are compatible

Python3
## Requires 
* You should have set sudo askpass (May change code to disable this. It will disable triggering of assistant by F8)
* Python3 is required and pip3 should be installed. (May work with python2 if certain changes are made)

## How to USE?
1. Download the source code (or clone) to your computer.
2. Run install.py from source. This installs required packages for Veronica

    ```There may be many errors as this utilises snowboy, a depreciated package.```
3. Run veronica.py. You are good to go. 

## Working
 * Run veronica.py. (Doesn't need to be in terminal may open command and open veronica. )
 * Enter Password. (Required to check if F8 is pressed)
 * Trigger wake word or press F8 to call veronica, it will hear your quesry and respond to it if any command is understood

## Generating personal pmdl file
Run this code in terminal which gives you an interface to record voice and create pmdl file.You must have docker installed.
> Make sure you choose a noiseless environment to prevent triggering false positives.  
  
   ```
   docker run -it -p 8000:8000 rhasspy/snowboy-seasalt
   ```
   
 This script is developed by rhasspy and link is given below.
  https://github.com/rhasspy/snowboy-seasalt

__After getting the pmdl file rename it to ```veronica.pmdl``` and save it in models directory in the source you have downloaded (or cloned). This is a must for wake word to work correctly__

## Why is it asking for password
 Veronica asks for password so that it can check if user presses F8. Veronica utilises keyboard module from python which needs root permission for checking keyboard events.It does not store or send any keyboard event, just checks if F8 is pressed. 

## Wake Word is not recognising 
* Make sure you have working microphone
* Make pmdl file properly. While making pmdl you should make sure it had included the wake word you said.
* You can change sensitivity and audio gain in veronica.py.  ```line 94``` This may improve ability of Veronica to recognise wake word. 

## Veronica triggering false positives
 While making pmdl you should have a noiseless environment. 

## Adding Personal Commands
You can add your personal command.For that,
1. Go to command_main.py and add a function and name in command_dict dictionary.
   > Format
   > ```python
   > {"commands":[command list],"func":function_name}
   > ```  
   > where command list is list of commands which will be commanded , and function_name is name of function to used later.
2. Now go to functions.py and define the function you had given in command_main.py
   > Add 
   > ```
   > def function_name():
   >    python code 
   > ```
3. This will add a function which will be triggered by commands with resemblence to commands list.


 ## To-Do 
 - [ ] Complete revamp needed with MCP (may be something like spotlight??)
