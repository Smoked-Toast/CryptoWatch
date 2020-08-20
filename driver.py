import time
import os
import requests
import bs4

from debugger import *

global Kill
Delay = 300

def run():
    #Global variable to determine if we should kill the program
    global Kill
    Kill = CheckKillSwitch()#Update kill switch

    LastRequest = [None]


    while (not Kill):
        Kill = CheckKillSwitch()#Update kill switch


        html_raw = requests.get("https://www.cryptofringe.com/rss").text
        ThisRequest = bs4.BeautifulSoup(html_raw, "html.parser")
        #print(ThisRequest.prettify())

        List = ThisRequest.channel.find_all("item")
        for x in List:
            title = x.title
            print(title)
            # description = x.description
            # print(description)


        time.sleep(Delay)
run()