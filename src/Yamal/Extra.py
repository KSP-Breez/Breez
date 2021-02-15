import sys
import time
import os
from enum import Enum
from Lexer import *

sender = os.path.basename(__file__)[:-3]
unfixedTime = time.asctime(time.localtime(time.time()))

class eventType(Enum):
    ERROR = 1
    GENERAL = 2
    START_END = 3
    

def Log(action, eventNumber):
    with open("log.ydl", "a") as YamalLogger:
        if eventNumber <= 10:
            event = eventType(int(eventNumber)).name
        else:
            return
                            
        YamalLogger.write(f"[{unfixedTime[4:]}]-[{sender}]-[{event}]: {action}.\n")
        
def errorMes(message, position="N/A"):
    Log(f"Error has occured while {sender[:-2]}ing at {position}, ERROR: {message}", 1)
    sys.exit(f"[{sender}]-[Position: {position}] | ERROR: {message}")