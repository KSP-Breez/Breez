from Lexer import *
from Logger import Log

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        
        self.curToken = None
        self.peekToken = None
        self.nextToken()
        self.nextToken()
    
    def checkToken(selk, kind):
        return kind == self.curToken.kind
    
    def checkPeek(self, kind):
        return kind == self.peekToken.kind
    
    def match(self, kind):
        if not self.checkToken(kind):
            errorMes(f"Expected: {kind.name}, got: {self.curToken.kind.name}")
        self.nextToken()
    
    def nextToken(self):
        self.curToken = self.peekToken
        self.peekToken = self.lexer.getToken()
        
    def program(self):
        Log("Starting parser")
        
        while not self.checkTOken(tokenType.EOF):
            self.statement()