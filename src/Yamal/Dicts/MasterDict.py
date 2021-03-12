from Suffixes.ShipDict import *
from Suffixes.testEnum import *
from enum import Enum

class MasterEnum(ShipEnum, TestEnum, Enum):
    ANOTHER_ENUM = 2100
    
print(MasterEnum)