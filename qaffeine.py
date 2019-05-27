#
# qaffeine - prevent inactivity on your computer by simulating key events
#
# Clem Lorteau - 2019-05-26

import sys
import os
import argparse
import pyautogui
from threading import Thread, Event

class KeyPressesSender(Thread):
    def __init__(self, event, key = 'altright'):
        Thread.__init__(self)
        self.key = key
        self.stopped = event    
    
    def run(self):
        while not self.stopped.wait(5):
            pyautogui.press(self.key)

if __name__ == '__main__':
    ap = argparse.ArgumentParser('Prevent computer inactivity by simulating key presses')
    ap.add_argument('-n','--nogui', action='store_true', help='Don\'t start a GUI, only a operate in text mode')
    ap.add_argument('-k', '--key', default = 'altright', help='Key to press [default: altright]; see keys.txt for a list of valid values')
    args = ap.parse_args()

    if args.nogui:
        stopFlag = Event()
        thread = KeyPressesSender(stopFlag, args.key)

        thread.start()
        input('Preventing inactivity; press <Enter> to stop...')
        stopFlag.set()

        sys.exit(0)
    
    else:
        pass
    