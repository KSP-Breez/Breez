import sys
import enum
from Tokens import *
from Extra import Log, errorMes, warningMes, generalMes, successMes



class Yamal_Lexer():
    def __init__(self, input):
        self.source = input + '\n'
        self.curChar = ''
        self.curPos = -1
        self.HorizPos = 1
        self.LastHorizPos = None
        self.VerticalPos = 1
        self.nextCharacter()
        
    def returnHorizPOS(self):
        if self.curChar != "\n":
            return self.LastHorizPos
        else:
            return self.HorizPos
    
    def nextCharacter(self):
        self.curPos += 1
        self.HorizPos += 1
        if self.curPos >= len(self.source):
            self.curChar = '\0' 
        else:
            self.curChar = self.source[self.curPos]
    
    def peek(self):
        if self.curPos + 1 >= len(self.source):
            return '\0'
        return self.source[self.curPos+1]
    
    #def errorMes(self, message):
    #    sys.exit(f"Error has occured while compiling at {curPos},{VerticalPos}!\nError: {message}")
    
    def skipSpaces(self):
        while self.curChar == ' ' or self.curChar == '\t' or self.curChar == '\r':
            self.HorizPos += 1
            self.nextCharacter()
    
    def skipComments(self):
        if self.curChar == "#":
            while self.curChar != "\n":
                self.nextCharacter()
    
    def getToken(self):
        token = None
        self.skipSpaces()
        self.skipComments()
        
        if self.curChar == "+":
            if self.peek() == "+":
                lastChar = self.curChar
                self.nextCharacter()
                token = Token(lastChar + self.curChar, tokenType.INCREMENT)
            else:
                token = Token(self.curChar, tokenType.PLUS)
            
        elif self.curChar == "-":
            if self.peek() == "-":
                lastChar = self.curChar
                self.nextCharacter()
                token = Token(lastChar + self.curChar, tokenType.DECREMENT)
            else:
                token = Token(self.curChar, tokenType.MINUS)
            
        elif self.curChar == '*':
            token = Token(self.curChar, tokenType.MULTIPLY)
            
        elif self.curChar == "/":
            token = Token(self.curChar, tokenType.DIVIDE)
            
        elif self.curChar == "^":
            if self.peek() == "^":
                lastChar = self.curChar
                self.nextCharacter()
                token = Token(lastChar + self.curChar, tokenType.ROUND)
            else:
                token = Token(self.curChar, tokenType.POWER)
        
        elif self.curChar == "=":
            if self.peek() == ">":
                lastChar = self.curChar
                self.nextCharacter()
                token = Token(lastChar + self.curChar, tokenType.DECLARE_EQUALS)
                
           # else if: self.peek() == "=":
               # token = Token(lastChar = self.curChar + self.curChar, tokenType.EQUALS_EQUALS)
            else:
                token = Token(self.curChar, tokenType.EQUALS)
                
        elif self.curChar == "%":
            token = Token(self.curChar, tokenType.MODULUS)
                
        elif self.curChar == "&":
            if self.peek() == "&":
                lastChar = self.curChar
                self.nextCharacter()
                token = Token(lastChar + self.curChar, tokenType.AND)
        
        elif self.curChar == "|":
            if self.peek() == "|":
                lastChar = self.curChar
                self.nextCharacter()
                token = Token(lastChar + self.curChar, tokenType.OR)
                
        elif self.curChar == ">":
            if self.peek() == "=":
                lastChar = self.curChar
                self.nextCharacter()
                token = Token(lastChar + self.curChar, tokenType.GREAT_OR_EQUALS)
            else:
                token = Token(self.curChar, tokenType.GREATER_THAN)
            
        elif self.curChar == "<":
            if self.peek() == "=":
                lastChar = self.curChar
                self.nextCharacter()
                token = Token(lastChar + self.curChar, tokenType.LESSER_OR_EQUALS)
            else:
                token = Token(self.curChar, tokenType.LESSER_THAN)
                            
        elif self.curChar == '$':
            # Get characters between quotations.
            self.nextCharacter()
            if self.curChar == "<":
                startPos = self.curPos
                while self.curChar != '>':
                    if self.peek() == '"' or self.peek() == "'":
                        errorMes('Template literal not closed, missing ">".', 1, self.HorizPos, self.VerticalPos)
                        sys.exit()
                        break
                        # ERROR: Loop refuses to exit even when sys.exit gets called inside the if statement.
                    self.nextCharacter()

            tokText = self.source[startPos : self.curPos] # Get the substring.
            token = Token(tokText, tokenType.TEMPLATE_LITERAL) 
            
        elif self.curChar == "@":
            token = Token(self.curChar, tokenType.AT_SYMBOL)
                
        elif self.curChar == "!":
            if self.peek() == "=":
                lastChar = self.curChar
                self.nextCharacter()
                token = Token(lastChar + self.curChar, tokenType.NOT_EQUALS)
                
            elif self.peek() == "!":
                lastChar = self.curChar
                self.nextCharacter()
                token = Token(lastChar + self.curChar, tokenType.MAX)
                
            else:
                errorMes("Unexpected token: !, Expected token: !=", 1, self.HorizPos, self.VerticalPos)
                
        elif self.curChar.isdigit():
            startPos = self.curPos
            while self.peek().isdigit():
                self.nextCharacter()
            if self.peek() == '.': # Floaty!
                self.nextCharacter()

                # Must have at least one digit after decimal.
                if not self.peek().isdigit(): 
                    # Error!
                    errorMes("Unexpected letter in floating point.", 1, self.HorizPos, self.verticalPos)
                while self.peek().isdigit():
                    self.nextCharacter()

            tokText = self.source[startPos : self.curPos + 1] # Get the substring.
            token = Token(tokText, tokenType.NUMBER)
                
        elif self.curChar == '"':
            startPos = self.curPos
            self.nextCharacter()
            
            while self.curChar != '"':
                self.nextCharacter()
                
            tokText = self.source[int(startPos) : int(self.curPos)] # Get the substring.
            token = Token(tokText, tokenType.STRING) 
            
        elif self.curChar.isalpha():
            # Leading character is a letter, so this must be an identifier or a keyword.
            # Get all consecutive alpha numeric characters.
            startPos = self.curPos
            while self.peek().isalnum():
                self.nextCharacter()

            # Check if the token is in the list of keywords.
            tokText = self.source[startPos : self.curPos + 1] # Get the substring.
            keyword = Token.checkIfKeyword(tokText)
            if keyword == None: # Identifier
                token = Token(tokText, tokenType.IDENT)
            else:   # Keyword
                token = Token(tokText, keyword)
            
        elif self.curChar == ";":
            token = Token(self.curChar, tokenType.EOL)
            
        elif self.curChar == "(":
            token = Token(self.curChar, tokenType.PARENTH_OPEN)
            
        elif self.curChar == ")":
            token = Token(self.curChar, tokenType.PARENTH_CLOSE)
            
        elif self.curChar == "{":
            token = Token(self.curChar, tokenType.CURLY_OPEN)
            
        elif self.curChar == "}":
            token = Token(self.curChar, tokenType.CURLY_CLOSE)
            
        elif self.curChar == ",":
            token = Token(self.curChar, tokenType.COMMA)
            
        elif self.curChar == ".":
            token = Token(self.curChar, tokenType.SUFFIX_SEP)
            
        elif self.curChar == ":":
            token = Token(self.curChar, tokenType.COLON)
        
        elif self.curChar == '\n':
            self.VerticalPos += 1
            self.LastHorizPos = self.HorizPos
            self.HorizPos = 0
            token = Token(self.curChar, tokenType.NEWLINE)
            
        elif self.curChar == '\0':
            token = Token(" ", tokenType.EOF)
                    
        else:
            errorMes(f"Unexpected token: {self.curChar} at {self.curPos}", 1, self.HorizPos, self.VerticalPos)
        
        self.nextCharacter()
        return token
        
class Token:   
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText
        self.kind = tokenKind
    @staticmethod
    def checkIfKeyword(tokenText):
        for kind in tokenType:
            # Relies on all keyword enum values being 1XX.
            if kind.name.lower() == tokenText and kind.value >= 100 and kind.value < 400:
                return kind
        return None
    
