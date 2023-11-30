# models/rol.py 

from enum import IntEnum , auto 

class Role (IntEnum): 
    NONE  = 0 
    ENEMY = auto() 
    ENTERANCE = auto() 
    EXIT =   auto() 
    EXTERIOR = auto() 
    REWARD =  auto() 
    WALL =  auto() 
    