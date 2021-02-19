from Lexer import *
from Extra import Log, errorMes

#globalPosition = __import__("Lexer").Yamal_Lexer.globalPosition

class Yamal_Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        
        self.vert = 0
        self.horiz = 0
        
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
            errorMes(f"Expected: {kind.name}, got: {self.curToken.kind.name}", 2, self.horiz, self.vert)
        self.nextToken()
    
    def nextToken(self):
        self.horiz += 1
        self.curToken = self.peekToken
        self.peekToken = self.lexer.getToken()
        
    def program(self):
        Log("Starting parser", 3, 2)
        print("PROGRAM")
        
        while self.checkToken(tokenType.NEWLINE):
            self.nextToken()
        
        while not self.checkToken(tokenType.EOF):
            self.statement()
            
    def expression(self):
        print("EXPRESSION")
        
        self.term()
        while self.checkToken(tokenType.PLUS) or self.checkToken(tokenType.MINUS):
            self.nextToken()
            self.term()
            
    def term(self):
        print("TERM")
        
        self.unary()
        while self.checkToken(tokenType.MULTIPLY) or self.checkToken(tokenType.DIVIDE):
            self.nextToken()
            self.unary()
            
    def unary(self):
        print("UNARY")
        
        if self.checkToken(tokenType.PLUS) or self.checkToken(tokenType.MINUS):
            self.nextToken()
        self.primary()
        
    """ def unaryOne(self):
        print("UNARY ONE")
        
        if self.checkToken(tokenType.INCREMENT) or self.checkToken(tokenType.DECREMENT):
            self.nextToken()
        self.primary() """
        
    def primary(self):
        print(f"PRIMARY ({self.curToken.text})")
        
        if self.checkToken(tokenType.NUMBER):
            self.nextToken()
        elif self.checkToken(tokenType.IDENT):
            self.nextToken()
        else:
            errorMes(f"Unexpected token at {self.globalPos} ({self.curToken.text})", 2, self.horiz, self.vert)
        
    def comparison(self):
        print("COMPARISON")
        
        self.expression()
        if self.isCompOP():
            self.nextToken()
            self.expression()
        else:
            errorMes(f"Expected comparison operator at {self.globalPos} ({self.curToken.text})", 2, self.horiz, self.vert) 
            
        while self.isCompOP():
            self.nextToken()
            self.expression()
            
    def isCompOP(self):
        return self.checkToken(tokenType.GREATER_THAN) or self.checkToken(tokenType.GREAT_OR_EQUALS) or self.checkToken(tokenType.LESSER_THAN) or self.checkToken(tokenType.LESSER_OR_EQUALS) or self.checkToken(tokenType.EQUALS) or self.checkToken(tokenType.NOT_EQUALS)
    
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
            self.comparison()
            
            self.match(tokenType.CURLY_OPEN)
            self.NL()
            
            while not self.checkToken(tokenType.CURLY_CLOSE):
                self.statement()
            
            self.match(tokenType.CURLY_CLOSE)
            
        elif self.checkToken(tokenType.WHILE):
            print("WHILE")
            self.nextToken()
            self.comparison()
            
            self.match(tokenType.CURLY_OPEN)
            self.NL()
            
            while not self.checkToken(tokenType.CURLY_CLOSE):
                self.statement()
                
            self.match(tokenType.CURLY_CLOSE)
            
        elif self.checkToken(tokenType.IDENT):
            print("VARIABLE")
            if self.checkPeek(tokenType.DECLARE_EQUALS):
                self.nextToken()
                self.match(tokenType.DECLARE_EQUALS)
                self.expression()
        
        # for i=>1,i<10,i++          
        elif self.checkToken(tokenType.FOR):        
            self.nextToken()
            self.match(tokenType.IDENT)
            self.match(tokenType.DECLARE_EQUALS)
            self.expression()
            
            self.match(tokenType.COMMA)
            
            self.comparison()
            
            self.match(tokenType.COMMA)
            
            self.expression()
            self.match(tokenType.CURLY_OPEN)
            self.NL()
            while not self.checkToken(tokenType.CURLY_CLOSE):
                self.statement()
            
            self.match(tokenType.CURLY_CLOSE)
                
        else:
            errorMes(f"Invalid statement at {self.globalPos} ({self.curToken.text}).", 2, self.horiz, self.vert)
            print(self.curToken.kind.name)
        
        self.EOL_NL()
            
    def EOL_NL(self):
        print("SEMICOLON + NEWLINE")
        self.vert += 1
        
        self.match(tokenType.EOL)
        self.match(tokenType.NEWLINE)
        while self.checkToken(tokenType.NEWLINE):
            self.nextToken()
    
    def NL(self):
        print("NEWLINE")
        self.vert += 1
        
        self.match(tokenType.NEWLINE)
        while self.checkToken(tokenType.NEWLINE):
            self.nextToken()