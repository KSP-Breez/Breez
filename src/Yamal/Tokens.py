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
    NOT = 16 # !
    AT_SYMBOL = 17 # @
    
    #-COMPILER DIRECTIVES-#
    
   # !!! Moved to its own category in #-KEYWORDS-# at 140 to 150 under #-DIRECTIVES-# tag
    
    #-KEYWORDS-#
    CPU = 100 # [0 - ARCHIVE], [1 - THIS CPU STORAGE]
    IF = 101
    WHILE = 102
    HOLD = 103
    PRINT = 104
    CLEAR = 105
    STAGE = 106
    ELSE = 107
    FOR = 108
    BREAK = 109
    THROTTLE = 110
    FALSE = 111
    TRUE = 112
    STEERING = 113
    GLOBAL = 114
    LOCAL = 115
    SHIP = 116
    LOG = 117
    RESTART = 118
    FUNC = 119
    UNLOCK = 120
    GOTO = 121
    
    # MISC
    UP = 122
    LABEL = 123
    LATLNG = 124
    DISTANCE = 125
    
    # META TAGS
    META = 126
    DESC = 127
    AUTHORS = 128
    LICENSE = 129
    
    # ACTION GROUPS
    AG1 = 130
    AG2 = 131
    AG3 = 132
    AG4 = 133
    AG5 = 134
    AG6 = 135
    AG7 = 136
    AG8 = 137
    AG9 = 138
    AG10 = 139
    
    # DIRECTIVES
    STRICT = 140
    IMPORT = 141
    LAZYGLOBAL = 142
    
    # OTHER KOS RELATED LANGUAGES TAGS
    KASM = 143
    GRAVITAS = 144
    KOS = 145
    
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