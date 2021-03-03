#!/usr/bin/env python3

# License: GNU General Public License V3
# Author: Darkuss

import os
import sys
import progress
import json
import time
from getpass import getuser

from Lexer import *
from Parser import *
from Emitter import *
from Extra import Log, errorMes, warningMes, generalMes, successMes, accessSettings, writeSettings

# with open("settings.json", "r+") as jsonObj:
#     Settings = json.load(jsonObj)
#     if Settings["firstTime?"] == 1:
#         Path = input("Please input the \033[4m full path\033[0m (Users/<Your username here>/) to your KSP folder here: ")
#         print(os.path.expanduser("~"))
#         Settings["KSPath"] = f"{Path}/Ships/Script".replace("/", "\\") if sys.platform == "win32" else f"{Path}/Ships/Script/" 
#         Settings["firstTime?"] = 0
#         jsonObj.seek(0)
#         json.dump(Settings, jsonObj, indent=4)
#         jsonObj.truncate()

def main():
    start = time.time()
    if len(sys.argv) != 2:
        errorMes("Yamal needs .briz source file as argument.", 4)
    if ".briz" in sys.argv[1]:
        with open(sys.argv[1], 'r') as yamalCompiler:
            writeSettings("CompilerIsStrict", 0)
            generalMes(f"Opened file {sys.argv[1]}", 3, 4)
        
            input = yamalCompiler.read()
        # Initialize the lexer and parser.
            lexer = Yamal_Lexer(input)
            emitter = Yamal_Emitter(f"{sys.argv[1][:-5]}_KS-OUT.ks")
            parser = Yamal_Parser(lexer, emitter, sys.argv[1])
    
            parser.program() # Start the parser.
            successMes("Parsing completed", 3, 2)
            emitter.output()
            
            end = time.time()
            
            successMes(f"Compilation complete, file saved to the current directory", 3, 4)
            generalMes(f"Summary: {parser.accessErrWarns()}", 2, 4)
            generalMes(f"Compilation time: {end - start}", 2, 4)
    else:
        errorMes("Yamal can't convert files with any extensions other than .briz", 4)
        
main() 
