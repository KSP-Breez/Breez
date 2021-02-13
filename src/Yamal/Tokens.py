import enum

class tokenType(enum.Enum):
    
    #-SPECIAL CHARACTERS-#
    
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3
    TEMPLATE_LITERAL = 4 # #<Variable> (Enclosed in double backticks rather than in single backticks)
    DECLARE_EQUALS = 5
    
    #-DIRECTIVES-#
    
    #-COMPILER DIRECTIVES-#
    
    STRICT = 51
    
    #-BREEZ DIRECTIVES-#
    
    IMPORT = 53
    LAZYGLOBAL = 54
    
    #-KEYWORDS-#
    
    IF = 101
    WHILE = 102
    HOLD = 103
    VAR = 104
    PRINT = 105
    CLEAR = 106
    STAGE = 107
    ELSE = 108
    UP = 109
    THROTTLE = 110
    FALSE = 111
    TRUE = 112
    SHIP = 113
    MASS = 114
    STEERING = 115
    G = 116
    L = 117
    FOR = 118
    AND = 119 # &&
    OR = 120 # ||
    
    
    #-MATHEMATICAL OPERATORS-#
    
    PLUS = 401 # +
    MINUS = 402 # -
    MULTIPLY = 403 # *
    DIVIDE = 404 # /
    MODULUS = 405 # %
    EQUALS =  406 # =
    NOT_EQUALS = 407 # !=
    GREATER_THAN = 408 # >
    LESSER_THAN = 409 # <
    GREAT_OR_EQUALS = 410 # >=
    LESSER_OR_EQUALS = 411 # <=
    SQUARE_ROOT = 412 # sqrt()
    POWER = 413 # ^
    
    