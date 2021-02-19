import sys
import time
import os
from enum import Enum
from Lexer import *

unfixedTime = time.asctime(time.localtime(time.time()))

class senderType(Enum):
    LEXER = 1
    PARSER = 2
    EMITTER = 3

class eventType(Enum):
    ERROR = 1
    GENERAL = 2
    START_END = 3
    
    
def returnOriginName(origin):
    if origin <= 3:
        originName = senderType(int(origin)).name
        return originName
    else:
        return 


def Log(action, eventNumber, origin):
    with open("log.ydl", "a") as YamalLogger:
        if eventNumber <= 10:
            event = eventType(int(eventNumber)).name.replace("_", "/")
        else:
            return
                              
        YamalLogger.write(f"[{unfixedTime[4:]}]-[{returnOriginName(origin)}]-[{event}]: {action}.\n")
        YamalLogger.write("-------------------------------------------------------------------\n")
        
def errorMes(message, sender, positionH="N/A", positionV="N/A"):
    Log(f"Error has occured while {returnOriginName(sender)[:-2].lower()}ing at {position}, ERROR: {message}", 1, int(sender))
    sys.exit(f"[{returnOriginName(sender)}]-[Position: {positionH},{positionV}]ERROR: {message}")