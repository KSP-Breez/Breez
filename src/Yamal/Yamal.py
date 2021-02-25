#!/usr/bin/env python3

import os
import sys
import progress
import json
import time

from Lexer import *
from Parser import *
from Emitter import *
from Extra import Log, errorMes, warningMes, generalMes, successMes

def main():
    start = time.time()
    if len(sys.argv) != 2:
        errorMes("Yamal needs .briz source file as argument.", 4)
    if ".briz" in sys.argv[1]:
        with open(sys.argv[1], 'r') as yamalCompiler:
            generalMes(f"Opened file {sys.argv[1]}", 3, 4)
        
            input = yamalCompiler.read()
        # Initialize the lexer and parser.
            lexer = Yamal_Lexer(input)
            emitter = Yamal_Emitter(f"{sys.argv[1][:-5]}_KS-OUT.ks")
            parser = Yamal_Parser(lexer, emitter, sys.argv[1])
    
            parser.program() # Start the parser.
            successMes("Parsing completed", 3, 2)
            emitter.output()
            successMes("Compiling complete, file saved to <placeholder>", 3, 4)
            end = time.time()
            print(end - start)
    else:
        errorMes("Yamal can't convert files with any extensions other than .briz", 4)
main() 
