#!/usr/bin/env python

import sys
import os
import feedparser
import time
import signal
sys.path.append(os.path.abspath("lib/"))
from UHScroll import *

UH.brightness(0.10)

def sigterm_handler(signal, frame):
    print 'DEBUG: SIGTERM received. Cleaning up HAT..'
    UH.clear()
    sys.exit(0)

# Cleanup HAT on SIGTERM (CTRL-C)
signal.signal(signal.SIGTERM, sigterm_handler)

def scroll(msg, color):
    unicorn_scroll(msg , color, 200,0.05)


#show_letter(special_smilie,'yellow',200)
    #colors = 'orange','blue','white','yellow','green','cyan','pink'
    #show_letter(special_hart,color,200)
    #time.sleep(0.17)


while True:
    azurestatusRSS = "https://azure.microsoft.com/en-us/status/feed/"
    feed = feedparser.parse(azurestatusRSS)
    print 'DEBUG: Fetching and parsing RSS..'

    if len(feed['items']) > 0:
        scroll(feed['channel']['title'], 'cyan')

        for item in feed['items']:
            scroll(item['title'], 'orange')
            scroll(item['description'], 'orange')

    else:
        #scroll('FULL HEALTH', 'green')
        #time.sleep(0.5)
        show_letter(special_smilie, 'green', 400)
        time.sleep(59)
