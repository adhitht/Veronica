import threading
import subprocess
import inspect
import distro
from datetime import datetime 
import setproctitle
#from fuzzywuzzy import process
from playsound import playsound
from googlesearch import search
import os

#System Imports
'''
try:
    try:
        from lib.snowboy import snowboydetect
    except:
        from snowboy import snowboydetect
except:
    import snowboydetect
'''
#Made 
import snowboydecoder
from functions import *
from command_main import getcommand
from speectotext import speechtotext
from search_app import get_app

