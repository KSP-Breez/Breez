from Lexer import *
from Emitter import *
import json
import os
from Extra import Log, errorMes, warningMes, generalMes, successMes

class Yamal_Parser:
    def __init__(self, lexer, emitter, sysargv):
        self.lexer = lexer
        self.emitter = emitter
        self.fileName = sysargv
        
        self.whileOperator = None
        
        self.invertedCOMP = {
            ">=": " <= ",
            "<=": " >= ",
            "=": " != ",
            "!=": " = ",
            "<": " > ",
            ">": " < "
        }
        self.metaInfo = {
            "Authors": "N/A",
            "Desc": "N/A",
            "License": "N/A"
        }
        
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
        with open("settings.json", "r") as sj: # Settings Json
            settings = json.load(sj)
            
            
            generalMes("Starting parser", 3, 2)
            self.emitter.headerLine(f"       //---Breez: {settings['Version']}---//")
            self.emitter.headerLine(f"      // Release: {settings['Release']}")
            self.emitter.headerLine(f"     // Source file: {self.fileName}")
            self.emitter.headerLine( "    //------------------------//")
            
            while self.checkToken(tokenType.NEWLINE):
                self.nextToken()
            
            while not self.checkToken(tokenType.EOF):
                self.statement()
                
            self.emitter.emitLine("wait until false.")
            
            self.emitter.headerLine(f"   // Authors: {self.metaInfo['Authors']}")
            self.emitter.headerLine(f"  // Description: {self.metaInfo['Desc']}")
            self.emitter.headerLine(f" // License: {self.metaInfo['License']}")
            self.emitter.headerLine( "// This file was compiled by Yamal transpiler")
            self.emitter.headerLine("\n")
                
            #for Alone in self.variablesAlone:
                #if Alone not in self.variables:
                    #warningMes(f"Variable has been declared but not used. Variable: {Alone}.", 2)
            
    def expression(self):
        
        self.term()
        while self.checkToken(tokenType.PLUS) or self.checkToken(tokenType.MINUS):
            self.emitter.emit(f" {self.curToken.text} ")
            self.nextToken()
            self.term()
            
    def term(self):
        
        self.unary()
        while self.checkToken(tokenType.MULTIPLY) or self.checkToken(tokenType.DIVIDE):
            self.emitter.emit(f" {self.curToken.text} ")
            self.nextToken()
            self.unary()
            
    def unary(self):
        unaryDict = {
            "+": "+",
            "-": "-",
            "++": "1 +",
            "--": "-1 +"
        }
        
        if self.checkToken(tokenType.PLUS) or self.checkToken(tokenType.MINUS) or self.checkToken(tokenType.INCREMENT) or self.checkToken(tokenType.DECREMENT):
            self.emitter.emit(f" {unaryDict[self.curToken.text]} ")
            self.nextToken()
        self.primary()
        
    def primary(self):
        
        if self.checkToken(tokenType.NUMBER):
            self.emitter.emit(self.curToken.text)
            self.nextToken()
        elif self.checkToken(tokenType.IDENT):
            #self.variablesAlone.remove(self.curToken.text)
            if self.curToken.text not in self.variables:
                errorMes(f"Non-existent variable: {self.curToken.text} at {self.lexer.returnHorizPOS()}, {self.vert}", 2, self.lexer.returnHorizPOS(), self.vert)
            self.emitter.emit(self.curToken.text)
            self.nextToken()
        else:
            errorMes(f"Unexpected token at {self.lexer.returnHorizPOS()},{self.vert} ({self.curToken.text})", 2, self.lexer.returnHorizPOS(), self.vert)
        
    def comparison(self):
        
        self.expression()
        if self.isCompOP():
            if self.whileOperator == True:
                self.emitter.emit(self.invertedCOMP[self.curToken.text])
            else:
                self.emitter.emit(f"{self.curToken.text} ")
            self.nextToken()
            self.expression()
        else:
            errorMes(f"Expected comparison operator at {self.lexer.returnHorizPOS}(),{self.vert} ({self.curToken.text})", 2, self.lexer.returnHorizPOS(), self.vert) 
            
        while self.isCompOP():
            if self.whileOperator == True:
                self.emitter.emit(self.invertedCOMP[self.curToken.text])
            else:
                self.emitter.emit(f"{self.curToken.text} ")
            self.nextToken()
            self.expression()
            
    def isCompOP(self):
        return self.checkToken(tokenType.GREATER_THAN) or self.checkToken(tokenType.GREAT_OR_EQUALS) or self.checkToken(tokenType.LESSER_THAN) or self.checkToken(tokenType.LESSER_OR_EQUALS) or self.checkToken(tokenType.EQUALS) or self.checkToken(tokenType.NOT_EQUALS)
    
    def statement(self):
        self.whileOperator = False
        
        if self.checkToken(tokenType.PRINT):
            self.nextToken()
            
            if self.checkToken(tokenType.STRING):
                self.emitter.emitLine(f'PRINT {self.curToken.text}".')
                self.nextToken()
            else:
                self.emitter.emit("PRINT ")
                self.expression()
                self.emitter.emitLine(".")
                
        elif self.checkToken(tokenType.IF):
            self.nextToken()
            self.emitter.emit("IF ")
            self.comparison()
            
            self.match(tokenType.CURLY_OPEN)
            self.NL()
            self.emitter.emitLine(" {")
            
            while not self.checkToken(tokenType.CURLY_CLOSE):
                self.statement()
                
            self.emitter.emitLine("}.")
            
            self.match(tokenType.CURLY_CLOSE)
            
        elif self.checkToken(tokenType.WHILE):
            self.whileOperator = True
            self.nextToken()
            self.emitter.emit("UNTIL")
            self.comparison()
            
            self.match(tokenType.CURLY_OPEN)
            self.NL()
            self.emitter.emitLine(" {")
            
            while not self.checkToken(tokenType.CURLY_CLOSE):
                self.statement()
                
            self.match(tokenType.CURLY_CLOSE)
            self.emitter.emitLine("}.")
            
        elif self.checkToken(tokenType.L):
            self.nextToken()
            
            if self.curToken.text not in self.variables:
                self.variables.add(self.curToken.text)
                #self.variablesAlone.add(self.curToken.text)
            
            self.emitter.emit(f"LOCAL {self.curToken.text} IS ")
            self.match(tokenType.IDENT)
            self.match(tokenType.DECLARE_EQUALS)
            if self.checkToken(tokenType.STRING):
                self.emitter.emitLine(f'{self.curToken.text}".')
                self.nextToken()
            else:
                self.expression()
                self.emitter.emitLine(".")
                
        elif self.checkToken(tokenType.G):
            self.nextToken()
            
            if self.curToken.text not in self.variables:
                self.variables.add(self.curToken.text)
                #self.variablesAlone.add(self.curToken.text)
            
            self.emitter.emit(f"GLOBAL {self.curToken.text} IS ")
            self.match(tokenType.IDENT)
            self.match(tokenType.DECLARE_EQUALS)
            if self.checkToken(tokenType.STRING):
                self.emitter.emitLine(f'{self.curToken.text}".')
                self.nextToken()
            else:
                self.expression()
                self.emitter.emitLine(".")
                
        # for i=>1,i<10,i++          
        elif self.checkToken(tokenType.FOR):
            self.whileOperator = True
            tempIdentStorage = None
            
            self.emitter.emit("FROM {") 
            self.nextToken()
            self.emitter.emit(f"LOCAL {self.curToken.text} IS ")
            self.variables.add(self.curToken.text)
            tempIdentStorage = self.curToken.text
            self.match(tokenType.IDENT)
            self.match(tokenType.DECLARE_EQUALS)
            self.expression()
            
            self.match(tokenType.COMMA)
            self.emitter.emit(".} UNTIL ")
            
            self.comparison()
            
            self.match(tokenType.COMMA)
            self.emitter.emit(f" STEP {{ SET {tempIdentStorage} TO")
            
            self.expression()
            self.emitter.emitLine(".} DO {")
            self.match(tokenType.CURLY_OPEN)
            self.NL()
            while not self.checkToken(tokenType.CURLY_CLOSE):
                self.statement()
            
            self.match(tokenType.CURLY_CLOSE)
            self.emitter.emitLine("}.")
            
        elif self.checkToken(tokenType.META):
            self.nextToken()
            self.match(tokenType.COLON)
            if self.checkToken(tokenType.AUTHORS):
                self.nextToken()
                self.match(tokenType.DECLARE_EQUALS)
                if self.checkToken(tokenType.STRING):
                    self.metaInfo["Authors"] = self.curToken.text[1:]
                    self.nextToken()
                else:
                    errorMes("Can't accept non-string values for metadata", 4, self.lexer.returnHorizPOS, self.vert)
            if self.checkToken(tokenType.DESC):
                self.nextToken()
                self.match(tokenType.DECLARE_EQUALS)
                if self.checkToken(tokenType.STRING):
                    self.metaInfo["Desc"] = self.curToken.text[1:]
                    self.nextToken()
                else:
                    errorMes("Can't accept non-string values for metadata", 4, self.lexer.returnHorizPOS, self.vert)
            if self.checkToken(tokenType.LICENSE):
                self.nextToken()
                self.match(tokenType.DECLARE_EQUALS)
                if self.checkToken(tokenType.STRING):
                    self.metaInfo["License"] = self.curToken.text[1:]
                    self.nextToken()
                else:
                    errorMes("Can't accept non-string values for metadata", 4, self.lexer.returnHorizPOS, self.vert)
                
        else:
            errorMes(f"Invalid statement at {self.lexer.returnHorizPOS()} ({self.curToken.text}).", 2, self.lexer.returnHorizPOS(), self.vert)
        
        self.EOL_NL()
            
    def EOL_NL(self):
        self.vert += 1
        
        self.match(tokenType.EOL)
        self.match(tokenType.NEWLINE)
        while self.checkToken(tokenType.NEWLINE):
            self.nextToken()
    
    def NL(self):
        self.vert += 1
        
        self.match(tokenType.NEWLINE)
        while self.checkToken(tokenType.NEWLINE):
            self.nextToken()