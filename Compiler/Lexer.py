import sys
import enum

sys.path.append("./Desktop/Projects/RealProjects/python-projects/Breez/Compiler")

from tokens import tokenType


class Yamal_Lexer():
    
    def __init__(self, input):
        self.source = input + '\n'
        self.curChar = ''
        self.curPos = -1
        self.nextCharacter()
    
    def nextCharacter(self):
        self.curPos += 1
        if self.curPos >= len(self.source):
            self.curChar = '\0' 
        else:
            self.curChar = self.source[self.curPos]
    
    def peek(self):
        if self.curPos + 1 >= len(self.source):
            return '\0'
        return self.source[self.curPos+1]
    
    def errorAndRunAway(self, message):
        sys.exit(f"Error has occured while compiling!\nError: {message}")
    
    def skipWhitespace(self):
        while self.curChar == ' ' or self.curChar == '\t' or self.curChar == '\r':
            self.nextCharacter()
    
    def skipComments(self):
        pass
    
    def getToken(self):
        token = None
        self.skipWhitespace()
        
        if self.curChar == "+":
            token = Token(self.curChar, tokenType.PLUS)
            
        elif self.curChar == "-":
            token = Token(self.curChar, tokenType.MINUS)
            
        elif self.curChar == '*':
            token = Token(self.curChar, tokenType.ASTERISK)
            
        elif self.curChar == "/":
            token = Token(self.curChar, tokenType.SLASH)
        
        elif self.curChar == "=":
            if self.peek() == ">":
                lastChar = self.curChar
                self.nextCharacter()
                token = Token(lastChar + self.curChar, tokenType.DECLARE_EQUALS)
                
           # else if: self.peek() == "=":
               # token = Token(self.lastChar + self.curChar, tokenType.EQUALS_EQUALS)
            else:
                token = Token(self.curChar, tokenType.EQUALS_EQUALS)
                
        elif self.curChar == ">":
            if self.peek() == "=":
                self.lastChar
                self.nextCharacter()
                token = Token(self.lastChar + self.curChar, tokenType.GREAT_OR_EQUALS)
            else:
                token = Token(self.curChar, tokenType.GREATER_THAN)
            
        elif self.curChar == "<":
            if self.peek() == "=":
                self.lastChar
                self.nextCharacter()
                token = Token(self.lastChar + self.curChar, tokenType.LESSER_OR_EQUALS)
            else:
                token = Token(self.curChar, tokenType.LESSER_THAN)
            
        elif self.curChar == "#":
            if self.peek() == "<":
                nextCharacter()
                while self.peek() != ">":
                    i = 0
                    i + 1
                    nextCharacter()
                    if self.peek() == ">":
                        token = Token(self.curChar, tokenType.TEMPLATE_LITERAL)
                    elif self.peek() == '"' or self.peek() == "'":
                        self.errorAndRunAway("Template literal not closed, missing \">\".")
                
        elif self.curChar == "d":
            print("e")
        elif self.curChar == "d":
            print("d")
        elif self.curChar == '\n':
            token = Token(self.curChar, tokenType.NEWLINE)
            
        elif self.curChar == '\0':
            token = Token(" ", tokenType.EOF)
        
        else:
            self.errorAndRunAway(f"Unexpected token: {self.curChar}")
        
        self.nextCharacter()
        return token
        
class Token:   
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText
        self.kind = tokenKind