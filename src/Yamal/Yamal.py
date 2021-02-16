#!/usr/bin/env python3

import os
import sys
import progress
from Lexer import *
from Parser import *
from Extra import Log, errorMes

def main():
    if len(sys.argv) != 2:
            sys.exit("Error: Compiler needs source file as argument.")
    with open(sys.argv[1], 'r') as yamalCompiler:
        Log(f"Opened file {sys.argv[1]}", 3)
        input = yamalCompiler.read()
    
        # Initialize the lexer and parser.
        lexer = Yamal_Lexer(input)
        parser = Yamal_Parser(lexer)

        parser.program() # Start the parser.
        Log("Parsing completed.", 3)
main()