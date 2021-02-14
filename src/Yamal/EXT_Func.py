import sys
import time
import os
from enum import Enum

sender = os.path.basename(__file__)[:-3]
unfixedTime = time.asctime(time.localtime(time.time()))

def Log(action, eventType):
    with open("log.ydl", "a") as YamalLogger:
        YamalLogger.write(f"[{unfixedTime[4:]}]-[{sender}]-[{eventType}]: {action}.\n")
        
def errorMes(self, message):
    sys.exit(f"[{sender}] | ERROR: {message}")
    Log()