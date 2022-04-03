__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"

from abc import ABC

from DAIDE.core import DaideObject
from DAIDE.core import Arrangement
from DAIDE.utils.parsing import consume, parse_with_parens

class Binop(DaideObject, ABC):
    """Abstract Base Class for BINOP DAIDE words like AND, ORR"""
    def __init__(self, arrangements):
        self.arrangements = arrangements

    def __str__(self):
        if len(self.arrangements) == 0:
            return ""
        elif len(self.arrangements) == 1:
            return str(self.arrangements[0])
        
        return self.__class__.__name__ + "".join([f" ({str(a)})" for a in self.arrangements])
    
    @classmethod
    def parse(cls, string):

        OP = string[:3]
        rest = string[3:]
        
        arrangements = []
        while rest[:2] == " (":
            rest = consume(rest, " ")
            
            arrangement, rest = parse_with_parens(rest, Arrangement)
            
            arrangements.append(arrangement)

        for subclass in Binop.__subclasses__():
            if subclass.__name__ == OP:
                return subclass(arrangements), rest

class AND(Binop):
    pass

class ORR(Binop):
    pass