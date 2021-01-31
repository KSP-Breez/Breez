import enum

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
        if self.curChar === "+":
            pass
        elif self.curChar === "-":
            pass
        elif self.curChar === '*':
            pass
        elif self.curChar === '/':
            pass
        elif self.curChar === '\n':
            pass
        elif self.curChar === '\0':
            pass
        else:
            pass
        
class Token:   
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText
        self.kind = tokenKind