import sys
import time
import os
from colorama import Fore, Style
from enum import Enum
from Lexer import *

unfixedTime = time.asctime(time.localtime(time.time()))

class senderType(Enum):
    LEXER = 1
    PARSER = 2
    EMITTER = 3
    YAMAL = 4

class eventType(Enum):
    ERROR = 1
    GENERAL = 2
    START_END = 3
    WARNING = 4
    
COLORS = {
    "ERROR": "\033[31m",
    "WARNING": "\033[38;5;80m",
    "SUCCESS": "\033[32m",
    "INFO": "\033[34m",
    "END": "\033[0m"
}
    
    
def returnOriginName(origin):
    if origin <= 10:
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
    Log(f"At {positionH},{positionV}, ERR: {message}", 1, int(sender))
    sys.exit(f"{COLORS['ERROR']}[{returnOriginName(sender)}]-[POS: {positionH},{positionV}] | ERROR: {message}{COLORS['END']}")
    
def warningMes(message, sender, positionH="N/A", positionV="N/A"):
    Log(f"At {positionH},{positionV}, WARN: {message}", 4, int(sender))
    print(f"{COLORS['WARNING']}[{returnOriginName(sender)}]-[POS: {positionH},{positionV}] | WARNING: {message}{COLORS['END']}")
    
def generalMes(message, eventNumber, sender):
    Log(message, eventNumber, int(sender))
    print(f"{COLORS['INFO']}[{returnOriginName(sender)}] | INFO: {message}{COLORS['END']}")

def successMes(message, eventNumber, sender):
    Log(message, 3, int(sender))
    print(f"{COLORS['SUCCESS']}[{returnOriginName(sender)}] | SUCCESS: {message}{COLORS['END']}")