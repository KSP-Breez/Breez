from Lexer import *
from Extra import Log, errorMes, warningMes, generalMes, successMes

class Yamal_Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        
        self.variables = set()
        self.variablesAlone = set()
        self.functions = set()
        #self.labelsGOTO = set()
        #self.labelsDECLARED = set()
        
        self.vert = 0
        #self.horiz = 0
        
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
            errorMes(r"Expected: {}, got: {}".format(kind.name, self.curToken.kind.name), 2, self.lexer.returnHorizPOS(), self.vert)
        self.nextToken()
    
    def nextToken(self):
        #self.horiz += 1
        self.curToken = self.peekToken
        self.peekToken = self.lexer.getToken()
        
    def program(self):
        generalMes("Starting parser", 3, 2)
        print("PROGRAM")
        
        while self.checkToken(tokenType.NEWLINE):
            self.nextToken()
        
        while not self.checkToken(tokenType.EOF):
            self.statement()
            
        #for Alone in self.variablesAlone:
            #if Alone not in self.variables:
                #warningMes(f"Variable has been declared but not used. Variable: {Alone}.", 2)
            
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
        print(r"PRIMARY ({})".format(self.curToken.text))
        
        if self.checkToken(tokenType.NUMBER):
            self.nextToken()
        elif self.checkToken(tokenType.IDENT):
            #self.variablesAlone.remove(self.curToken.text)
            if self.curToken.text not in self.variables:
                errorMes(f"Non-existent variable: {self.curToken.text} at {self.lexer.returnHorizPOS()}, {self.vert}", 2, self.lexer.returnHorizPOS(), self.vert)
            self.nextToken()
        else:
            errorMes(f"Unexpected token at {self.lexer.returnHorizPOS()},{self.vert} ({self.curToken.text})", 2, self.lexer.returnHorizPOS(), self.vert)
        
    def comparison(self):
        print("COMPARISON")
        
        self.expression()
        if self.isCompOP():
            self.nextToken()
            self.expression()
        else:
            errorMes(f"Expected comparison operator at {self.lexer.returnHorizPOS}(),{self.vert} ({self.curToken.text})", 2, self.lexer.returnHorizPOS(), self.vert) 
            
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
            
            if self.curToken.text not in self.variables:
                self.variables.add(self.curToken.text)
                #self.variablesAlone.add(self.curToken.text)
            
            if self.checkPeek(tokenType.DECLARE_EQUALS):
                self.nextToken()
                self.match(tokenType.DECLARE_EQUALS)
                self.expression()
            else:
                errorMes("Missing declaration operator (=>).", 1, self.lexer.returnHorizPOS(), self.vert)
        
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
            errorMes(f"Invalid statement at {self.lexer.returnHorizPOS()} ({self.curToken.text}).", 2, self.lexer.returnHorizPOS(), self.vert)
            print(self.curToken.kind.name)
        
        self.EOL_NL()
            
    def EOL_NL(self):
        print("SEMICOLON + NEWLINE")
        self.vert += 1
        #self.horiz = 0
        
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