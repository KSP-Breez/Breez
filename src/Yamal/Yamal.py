import os
import sys
import progress
from Lexer import *
from Logger import Log


def main():
    if len(sys.argv) != 2:
            sys.exit("Error: Compiler needs source file as argument.")
    with open(sys.argv[1], 'r') as yamalCompiler:
        Log(f"Opened file {sys.argv[1]}")
        input = yamalCompiler.read()
    
        # Initialize the lexer and parser.
        lexer = Lexer(input)
        parser = Parser(lexer)

        parser.program() # Start the parser.
        Log("Parsing completed.")

def read():
    input = 'if"Pogchamp it is a string" @LAZYGLOBAL: @IMPORT: @STRICT: */+- 123 456.789 while print poggers #<TEST> g l'
    lexer = Yamal_Lexer(input)
    
    token = lexer.getToken()
    
    while token.kind != tokenType.EOF:
        print(token.kind)
        token = lexer.getToken()

read()