import enum

class tokenType(enum.Enum):
    
    #-SPECIAL CHARACTERS-#
    
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3
    
    #-KEYWORDS-#
    
    IF = 101
    WHILE = 102
    WAIT = 103
    #VAR_L = 104 - Useless for now
    #VAR_G = 105 - Useless for now
    VAR = 104
    PRINT = 105
    CLEAR = 106
    STAGE = 107
    ELSEIF = 108
    WAIT_UNTIL = 109
    THROTTLE = 110
    FALSE = 111
    TRUE = 112
    SHIP = 113
    MASS = 114
    STEERING 115
    UP = 116
    LANDED = 117
    
    #-MATHEMATICAL OPERATORS-#
    
    PLUS = 201 
    MINUS = 202
    ASTERISK = 203
    SLASH = 204
    EQUALS_EQUALS =  205
    NOT_EQUALS = 206
    GREATER_THAN = 207
    LESSER_THAN = 208
    GREAT_OR_EQUALS = 211
    LESSER_OR_EQUALS = 210
    
    #-DECLARE OPERATORS-#
    
    DECLARE_EQUALS = 301
    
    