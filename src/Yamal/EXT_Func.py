import sys
import time
import os
from enum import Enum

sender = os.path.basename(__file__)[:-3]
unfixedTime = time.asctime(time.localtime(time.time()))

class eventType(Enum):
    ERROR = 1
    START_END = 2
    

def Log(action, eventType):
    with open("log.ydl", "a") as YamalLogger:
        for kind in tokenType:
            # Relies on all keyword enum values being 1XX.
            if kind.name.lower() == tokenText and kind.value >= 100 and kind.value < 400:
                return kind
        YamalLogger.write(f"[{unfixedTime[4:]}]-[{sender}]-[{eventType}]: {action}.\n")
        
def errorMes(self, message):
    Log()
    sys.exit(f"[{sender}] | ERROR: {message}")