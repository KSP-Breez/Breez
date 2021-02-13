import sys
import time
import os

unfixedTime = time.asctime(time.localtime(time.time()))

def Log(action):
    with open("log.ydl", "a") as YamalLogger:
        YamalLogger.write(f"[{unfixedTime[4:]}]--[{os.path.basename(__file__)}]--[EVENT]: {action}.\n")
        
Log("Detected a program, booting up lexer")