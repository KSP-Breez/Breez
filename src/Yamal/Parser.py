from Lexer import *
from Extra import Log, errorMes

class Yamal_Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        
        self.curToken = None
        self.peekToken = None
        self.nextToken()
        self.nextToken()
    
    def checkToken(self, kind):
        return kind == self.curToken.kind
    
    def checkPeek(self, kind):
        return kind == self.peekToken.kind
    
    def match(self, kind):
        if not self.checkToken(kind):
            errorMes(f"Expected: {kind.name}, got: {self.curToken.kind.name}", 2)
        self.nextToken()
    
    def nextToken(self):
        self.curToken = self.peekToken
        self.peekToken = self.lexer.getToken()
        
    def program(self):
        Log("Starting parser", 3, 2)
        print("PROGRAM")
        
        while not self.checkToken(tokenType.EOF):
            self.statement()
    
    def statement(self):
        if self.checkToken(tokenType.PRINT):
            print("PRINT")
            self.nextToken()
            
            if self.checkToken(tokenType.STRING):
                self.nextToken()
            else:
                self.expression()
                
        elif self.checkToken(tokenType.IF):
            print("IF")
            self.nextToken()
            self.comparison
            
            self.match(tokenType.CURLY_OPEN)
            self.NL()
            
            while not self.checkToken(tokenType.CURLY_CLOSE):
                self.statement()
            
            self.mach(tokenType.CURLY_CLOSE)
            
        elif self.checkToken(tokenType.WHILE):
            print("WHILE")
            self.nextToken()
            self.comparison()
            
            self.match(tokenType.CURLY_OPEN)
            self.NL()
            
            while not self.checkToken(tokenType.CURLY_CLOSE)
                self.statement()
                
            self.match(tokenType.CURLY_CLOSE)
            
        elif self.checkToken(tokenType.IDENT):
            print("IDENT")
            if self.checkPeek(tokenType.DECLARE_EQUALS):
                self.nextToken()
                self.match(tokenType.DECLARE_EQUALS)
                self.expression()
        
        
        self.EOL_NL()
            
    def EOL_NL(self):
        print("SEMICOLON + NEWLINE")
        
        self.match(tokenType.EOL)
        self.match(tokenType.NEWLINE)
        while self.checkToken(tokenType.NEWLINE):
            self.nextToken()
    
    def NL(self):
        print("NEWLINE")
        
        self.match(tokenType.NEWLINE)
        while self.checkToken(tokenType.NEWLINE):
            self.nextToken()