#!/usr/bin/env python

import sys
import os
import feedparser
import time
sys.path.append(os.path.abspath("lib/"))
from UHScroll import *

UH.brightness(0.10)

def scroll(msg, color):
    unicorn_scroll(msg , color, 200,0.05)


#show_letter(special_smilie,'yellow',200)
    #colors = 'orange','blue','white','yellow','green','cyan','pink'
    #show_letter(special_hart,color,200)
    #time.sleep(0.17)


while True:
    azurestatusRSS = "https://azure.microsoft.com/en-us/status/feed/"
    feed = feedparser.parse(azurestatusRSS)

    scroll(feed['channel']['title'], 'cyan')

    if len(feed['items']) > 0:
        for item in feed['items']:
            scroll(item['title'], 'orange')
            scroll(item['description'], 'orange')
    else:
        scroll('FULL HEALTH', 'green')
        time.sleep(0.5)
        show_letter(special_smilie, 'green', 400)
