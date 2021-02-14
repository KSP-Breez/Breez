import os
import sys
import progress
from Lexer import *
from Parser import *
from Logger import Log


def main():
    if len(sys.argv) != 2:
            sys.exit("Error: Compiler needs source file as argument.")
    with open(sys.argv[1], 'r') as yamalCompiler:
        Log(f"Opened file {sys.argv[1]}")
        input = yamalCompiler.read()
    
        # Initialize the lexer and parser.
        lexer = Yamal_Lexer(input)
        parser = Yamal_Parser(lexer)

        parser.program() # Start the parser.
        Log("Parsing completed.")
main()