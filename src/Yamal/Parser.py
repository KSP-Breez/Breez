from Lexer import *
from Emitter import *
import os
from Extra import *

class Yamal_Parser:
    def __init__(self, lexer, emitter, sysargv):
        self.lexer = lexer
        self.emitter = emitter
        self.fileName = sysargv
        
        self.whileOperator = None
        self.identLevel = 0
        
        self.errorCount = 0
        self.warningCount = 0
        
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
        self.RAM = {}
        self.SEC_RAM = {}
        
        self.variables = set()
        self.variablesAlone = set()
        self.functions = set()
        self.functionsCalled = set()
        
        self.funcParameters = set()
        
        self.vert = 1
        #self.horiz = 0
        
        self.curToken = None
        self.peekToken = None
        self.nextToken()
        self.nextToken()
    
    def checkToken(self, kind):
        return kind == self.curToken.kind
    
    def returnSuffix(self, suffxiName):
        pass
    
    def accessRAM(self, RAM_Number):
        #RAMLog(RAM_Number, "R")
        return self.RAM[RAM_Number]
    
    def addToRAM(self, RAM_Ident, funcParameter): #, funcParValue):
        self.RAM[RAM_Ident] = funcParameter
        #self.RAM[f"{RAM_Ident}_Value"] = funcParValue
        #RAMLog(RAM_Ident, "W")
        
    def accessSecondaryRAM(self, FunctionName):
        return self.SEC_RAM[FunctionName]
        
    def addToSecondaryRAM(self, FunctionName, numOfPar):
        self.SEC_RAM[FunctionName] = numOfPar
        
    def accessErrWarns(self):
        return f"Errors: {self.errorCount}, Warnings: {self.warningCount}"
    
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
        self.emitter.headerLine(f"       //---Breez: {accessSettings('Version')}---//")
        self.emitter.headerLine(f"      // Release: {accessSettings('Release')}")
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
    

        for function in self.functionsCalled:
            if function not in self.functions:
                errorMes(f"Attempting to call a non-existent function: {function}", 2, self.lexer.returnHorizPOS(), self.vert)
                      
        for possibleAlone in self.variablesAlone:
            if possibleAlone in self.variables:
                if accessSettings("CompilerIsStrict") == 0:
                    self.warningCount += 1
                    warningMes(f"Non-used used variable: {possibleAlone}", 2, self.lexer.returnHorizPOS(), self.vert)
                elif accessSettings("CompilerIsStrict") == 1:
                    self.errorCount += 1
                    errorMes(f"Non-used used variable: {possibleAlone}", 2, self.lexer.returnHorizPOS(), self.vert)
        for functionsAlone in self.functions:
            if functionsAlone not in self.functionsCalled:
                if accessSettings("CompilerIsStrict") == 0:
                    self.warningCount += 1
                    warningMes(f"Non-used used function: {functionsAlone}", 2, self.lexer.returnHorizPOS(), self.vert)
                elif accessSettings("CompilerIsStrict") == 1:
                    self.errorCount += 1
                    errorMes(f"Non-used used function: {functionsAlone}", 2, self.lexer.returnHorizPOS(), self.vert)
            
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
            if self.curToken.text in self.variablesAlone:
                self.variablesAlone.remove(self.curToken.text)
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
        tempFunctionStor = None
        self.emitter.emit("    "*self.identLevel)
        RAM_ID = 0
        
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
            
            self.identLevel += 1
            while not self.checkToken(tokenType.CURLY_CLOSE):
                self.statement()
            self.identLevel -= 1 
            
            self.emitter.emitLine("}.")
            
            self.match(tokenType.CURLY_CLOSE)
            
        elif self.checkToken(tokenType.STAGE):
            self.nextToken()
            self.emitter.emitLine("STAGE.")
            self.match(tokenType.PARENTH_OPEN)
            self.match(tokenType.PARENTH_CLOSE)
            
        elif self.checkToken(tokenType.WHILE):
            self.whileOperator = True
            self.nextToken()
            self.emitter.emit("UNTIL")
            self.comparison()
            
            self.match(tokenType.CURLY_OPEN)
            self.NL()
            self.emitter.emitLine(" {")
            
            self.identLevel += 1
            while not self.checkToken(tokenType.CURLY_CLOSE):
                self.statement()
            self.identLevel -= 1 
                
            self.match(tokenType.CURLY_CLOSE)
            self.emitter.emitLine("}.")
            
        elif self.checkToken(tokenType.L):
            self.nextToken()
            
            if self.curToken.text not in self.variablesAlone:
                self.variablesAlone.add(self.curToken.text)
            
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
            
            if self.curToken.text not in self.variablesAlone:
                self.variablesAlone.add(self.curToken.text)
            
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
            self.match(tokenType.L)
            self.emitter.emit(f"LOCAL {self.curToken.text} IS ")
            if self.curToken.text not in self.variablesAlone:
                self.variablesAlone.add(self.curToken.text)
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
            
            self.identLevel += 1
            while not self.checkToken(tokenType.CURLY_CLOSE):
                self.statement()
            self.identLevel -= 1 
            
            self.match(tokenType.CURLY_CLOSE)
            self.emitter.emitLine("}.")
            
        elif self.checkToken(tokenType.META):
            self.nextToken()
            self.match(tokenType.SUFFIX_SEP)
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
                    
        elif self.checkToken(tokenType.AT_SYMBOL):
            self.nextToken()
            
            if self.checkToken(tokenType.STRICT):
                self.nextToken()
                writeSettings("CompilerIsStrict", 1)
                
                
            elif self.checkToken(tokenType.IMPORT):
                self.nextToken()
                self.match(tokenType.COLON)
                if self.checkToken(tokenType.STRING) and self.curToken.text[1:].startswith("ARCHIVE:/") or \
                self.checkToken(tokenType.STRING) and self.curToken.text[1:].startswith("MEMORY:/"):
                    self.emitter.emitLine(f'RUNONCEPATH("{self.curToken.text[1:].replace("MEMORY", "1") if self.curToken.text[1:].startswith("MEMORY:/", 0, 8) else self.curToken.text[1:].replace("ARCHIVE", "0")}").')
                    self.match(tokenType.STRING)
                    
                    
            elif self.checkToken(tokenType.LAZYGLOBAL):
                if self.checkPeek(tokenType.TRUE) or self.checkPeek(tokenType.FALSE):
                    self.nextToken()
                    self.emitter.emitLine(f"@LAZYGLOBAL {self.curToken.text}".replace("true", "ON") \
                    if self.curToken.text == "true" else f"@LAZYGLOBAL {self.curToken.text}".replace("false", "OFF"))
                    self.nextToken()
        
        elif self.checkToken(tokenType.IDENT):
            if self.checkPeek(tokenType.PARENTH_OPEN):
                CounterOfPar = 0
                self.functionsCalled.add(self.curToken.text)
                tempFunctionStor = self.curToken.text
                NumOfPar = self.accessSecondaryRAM(tempFunctionStor)
                self.emitter.emit(self.curToken.text)
                self.nextToken()
                self.emitter.emit("(")
                self.match(tokenType.PARENTH_OPEN)
                
                while self.checkToken(tokenType.IDENT) or self.checkToken(tokenType.COMMA):
                    self.emitter.emit(self.curToken.text)
                    self.match(tokenType.IDENT)
                    if not self.checkToken(tokenType.PARENTH_CLOSE):
                        self.emitter.emit(", ")
                        self.match(tokenType.COMMA)
                    CounterOfPar += 1
                if CounterOfPar > NumOfPar:
                    errorMes("Cannot accept more function parameters than defined in function declaration", 2, self.lexer.returnHorizPOS(), self.vert)
                elif CounterOfPar < NumOfPar:
                    errorMes("Missing function parameters", 2, self.lexer.returnHorizPOS(), self.vert)
                self.match(tokenType.PARENTH_CLOSE)
                self.emitter.emitLine(").")
            
        elif self.checkToken(tokenType.FUNC):
            self.emitter.emit("FUNCTION ")
            self.nextToken()
            tempFunctionStor = self.curToken.text
            if self.curToken.text not in self.functions:
                self.functions.add(self.curToken.text)
            self.emitter.emit(self.curToken.text)
            self.match(tokenType.IDENT)
            self.match(tokenType.PARENTH_OPEN)
            while self.checkToken(tokenType.IDENT) or self.checkToken(tokenType.COMMA):
                self.addToRAM(f"{tempFunctionStor}{RAM_ID}", self.curToken.text)
                self.match(tokenType.IDENT)
                if not self.checkToken(tokenType.PARENTH_CLOSE):
                    self.match(tokenType.COMMA)
                RAM_ID += 1
            self.match(tokenType.PARENTH_CLOSE)
            self.emitter.emitLine(" {")
            self.match(tokenType.CURLY_OPEN)
            self.NL()
            for RAM_Iter in range(RAM_ID):
                nextIdentLevel = self.identLevel + 1
                self.emitter.emitLine("    "*nextIdentLevel + f"PARAMETER {self.accessRAM(f'{tempFunctionStor}{RAM_Iter}')}.")
            self.addToSecondaryRAM(tempFunctionStor, RAM_ID)
            
            self.identLevel += 1
            while not self.checkToken(tokenType.CURLY_CLOSE):
                self.statement()
            self.identLevel -= 1 
                
            self.match(tokenType.CURLY_CLOSE)
            self.emitter.emitLine("}.")            
                
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