import enum

class tokenType(enum.Enum):
    
    #-SPECIAL CHARACTERS-#
    
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3
    TEMPLATE_LITERAL = 4 # $<Variable> (Enclosed in double backticks rather than in single backticks)
    DECLARE_EQUALS = 5 # =>
    EOL = 6 # ;
    CURLY_OPEN = 7
    CURLY_CLOSE = 8
    PARENTH_OPEN = 9
    PARENTH_CLOSE = 10
    COMMA = 11 # ,
    SUFFIX_SEP = 12
    COLON = 13
    AND = 14 # &&
    OR = 15 # ||
    AT_SYMBOL = 16 # @
    
    #-COMPILER DIRECTIVES-#
    
   # !!! Moved to its own category in #-KEYWORDS-# at 140 to 150 under #-DIRECTIVES-# tag
    
    #-KEYWORDS-#
    CPU = 102 # [0 - ARCHIVE], [1 - THIS CPU STORAGE]
    IF = 103
    WHILE = 104
    HOLD = 105
    PRINT = 106
    CLEAR = 107
    STAGE = 108
    ELSE = 109
    FOR = 110
    BREAK = 111
    THROTTLE = 112
    FALSE = 113
    TRUE = 114
    STEERING = 115
    G = 116
    L = 117
    PRINTAT = 118
    LOG = 119
    TO = 120
    RESTART = 121
    FUNC = 122
    UNLOCK = 123
    
    # MISC
    UP = 121
    LABEL = 122
    LATLNG = 123
    DISTANCE = 124
    
    # META TAGS
    META = 125
    DESC = 126
    AUTHORS = 127
    LICENSE = 128
    
    # ACTION GROUPS
    AG1 = 129
    AG2 = 130
    AG3 = 131
    AG4 = 132
    AG5 = 133
    AG6 = 134
    AG7 = 135
    AG8 = 136
    AG9 = 137
    AG10 = 138
    
    # DIRECTIVES
    STRICT = 140
    IMPORT = 141
    LAZYGLOBAL = 142
    
    #-MATHEMATICAL OPERATOR-S#
    
    PLUS = 1001 # +
    MINUS = 1002 # -
    MULTIPLY = 1003 # *
    DIVIDE = 1004 # /
    MODULUS = 1005 # %
    EQUALS =  1006 # =
    NOT_EQUALS = 1007 # !=
    GREATER_THAN = 1008 # >
    LESSER_THAN = 1009 # <
    GREAT_OR_EQUALS = 1010 # >=
    LESSER_OR_EQUALS = 1011 # <=
    SQUARE_ROOT = 1012 # sqrt()
    POWER = 1013 # ^
    INCREMENT = 1014 # ++
    DECREMENT = 1015 # --
    ROUND = 1016 # ^^
    MIN = 1017 # ??
    MAX = 1018 # !!