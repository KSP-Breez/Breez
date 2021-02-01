import enum
from Tokens import *

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
    
    def errorAbort(self, message):
        pass
    
    def skipWhitespace(self):
        pass
    
    def skipComments(self):
        pass
    
    def getToken(self):
        token = None
        
        if self.curChar === "+":
            token = Token(self.curChar, tokenType.PLUS)
            
        elif self.curChar === "-":
            token = Token(self.curChar, tokenType.MINUS)
            
        elif self.curChar === '*':
            token = Token(self.curChar, tokenType.ASTERISK)
            
        elif self.curChar === '/':
            token = Token(self.curChar, tokenType.SLASH)
            
        elif self.curChar === '\n':
            token = Token(self.curChar, tokenType.NEWLINE)
            
        elif self.curChar === '\0':
            token = Token(self.curChar, tokenType.EOF)
        
        else:
            pass
        
class Token:   
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText
        self.kind = tokenKind