import sys
import time
import os
import json
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "YES"
import pygame
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
    "WARNING": "\033[38;5;214m",
    "SUCCESS": "\033[38;5;42m", # 32m - standard value
    "INFO": "\033[38;5;39m",
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
        
def accessSettings(setting):
    with open("settings.json", "r") as settings:
        settingsObj = json.load(settings)
        return settingsObj[setting]
    
def writeSettings(setting, value):
    with open("settings.json", "r+") as settings:
        settingsObj = json.load(settings)
        settingsObj[setting] = value
        settings.seek(0)
        json.dump(settingsObj, settings, indent=4)
        settings.truncate()
     
# !!! WARNING: DO NOT USE UNLESS YOU WANT TO SEE HOW THE COMPILER WRITES AND READ FROM "VIRTUAL RAM"!
        
def RAMLog(RAM_Number, W_D_R): # W - Write, D - Delete, R - Read
    with open("RAMLog.ydl", "a") as RAMLogger:
        ActionDict = {
            "W": "[Write] - Added",
            "D": "[Delete] - Cleared",
            "R": "[Read] - Read"
        }
        
        if W_D_R == "R" or W_D_R == "W":
            RAMLogger.write(f"{ActionDict[W_D_R]} value from {RAM_Number}.\n")
        else:
            RAMLogger.write(f"{ActionDict[W_D_R]} RAM on startup.\n")
        
def errorMes(message, sender, positionH="N/A", positionV="N/A"):
    Log(f"At {positionH},{positionV}, ERR: {message}", 1, int(sender))
    with open("settings.json", "r") as setRead:
        errorSoundEnabled = json.load(setRead)
        if errorSoundEnabled["errorSoundEnabled?"] == 1:
            pygame.mixer.init()
            pygame.mixer.music.load("error.wav")
            pygame.mixer.music.play()
    time.sleep(0.18) # * It only works if we do it like this, so please don't change it 
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