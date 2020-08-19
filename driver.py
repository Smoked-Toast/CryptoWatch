import time
import os
import csv

from debugger import *

global Kill

def run():
    #Global variable to determine if we should kill the program
    global Kill
    Kill = CheckKillSwitch()#Update kill switch


    while (not Kill):
        time.sleep(1)
        Kill = CheckKillSwitch()#Update kill switch
        print(Kill)

run()