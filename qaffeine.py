#
# qaffeine - prevent inactivity on your computer by simulating key presses
#
# Clem Lorteau - 2019-05-26

import sys
import argparse
from threading import Thread, Event
from PySide2.QtCore import QCoreApplication, QEvent, Qt
from PySide2.QtGui import QKeyEvent
from PySide2.QtWidgets import QMainWindow, QApplication

class KeyPressesSender(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event
        self.invisible = QMainWindow()
    
    def run(self):
        while not self.stopped.wait(0.5):
            print('Send')
            sendEvent = QKeyEvent(QEvent.KeyPress, Qt.Key_F15, Qt.NoModifier)
            QCoreApplication.postEvent(self.invisible, sendEvent)
            self.stopped.wait(0.1)
            sendEvent = QKeyEvent(QEvent.KeyRelease, Qt.Key_F15, Qt.NoModifier)
            QCoreApplication.postEvent(self.invisible, sendEvent)

if __name__ == '__main__':
    ap = argparse.ArgumentParser('Prevent computer inactivity')
    ap.add_argument('-n','--nogui', help='Don\'t start a GUI, only a operate in text mode', action='store_true')
    args = ap.parse_args()

    if args.nogui:
        app = QApplication(sys.argv) #JUST FOR TEST
        stopFlag = Event()
        thread = KeyPressesSender(stopFlag)
        thread.start()

        sys.exit(app.exec_()) #JUST FOR TEST
        #sys.exit(0)
    
    else:
        pass
    