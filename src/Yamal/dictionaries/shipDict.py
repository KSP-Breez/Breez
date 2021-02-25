import enum

class shipSuffix(enum.Enum):
    """
    This Enum class contains various suffixes for [SHIP] built-in variable
    """
    MAXTHRUST = 1
    HEADING = 2
    FACING = 3
    AVAILABLETHRUST = 4
    MASS = 5
    WETMASS = 6
    DRYMASS = 7
    Q = 8
    VERTICALSPEED = 9
    GROUNDSPEED = 10
    AIRSPEED = 11
    NAME = 12
    STATUS = 13
    TYPE = 14
    LOADED = 15
    UNPACKED = 16
    CREW = 17
    MESSAGES = 18
    
    
class resourceSuffix(enum.Enum):
    """
    This Enum class contains various suffixes for [RESOURCES] suffix
    """
    KEROSENE = 1
    LIQUIDFUEL = 2
    OXIDIZER = 3
    MONOPROP = 4
    ELECTRICCHARGE = 5
    