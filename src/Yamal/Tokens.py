import enum

class tokenType(enum.Enum):
    
    #-SPECIAL CHARACTERS-#
    
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3
    TEMPLATE_LITERAL = 4 # #<Variable> (Enclosed in double backticks rather than in single backticks)
    DECLARE_EQUALS = 5 # =>
    EOL = 6 # ;
    CURLY_OPEN = 7
    CURLY_CLOSE = 8
    PARENTH_OPEN = 9
    PARENTH_CLOSE = 10
    
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
    THROTTLE_ = 110
    FALSE = 111
    TRUE = 112
    STEERING_ = 113
    G = 114
    L = 115
    FOR = 116
    AND = 117 # &&
    OR = 118 # ||
    PRINTAT = 119
    
    
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
    
    