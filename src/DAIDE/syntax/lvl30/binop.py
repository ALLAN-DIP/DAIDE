__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"

from abc import ABC, abstractmethod

from DAIDE.syntax.DAIDE_OBJECT import DAIDE_OBJECT
from DAIDE.utils.exceptions import ParseError
from DAIDE.utils.parsing import consume 

class BINOP(DAIDE_OBJECT, ABC):
    """Abstract Base Class for BINOP DAIDE words like AND, ORR"""
    def __init__(self, arrangements, OP):
        self.arrangements = arrangements
        self.OP = OP

    def __str__(self):
        if len(self.arrangements) == 0:
            return ""
        elif len(self.arrangements) == 1:
            return self.arrangements[0]
        
        return self.OP + "".join([f" ({a})" for a in self.arrangements])
    
    @classmethod
    def parse(cls, string, OP):
        
        rest = consume(string, OP)
        
        arrangements = []
        try:
            while True:
                rest = consume(rest, " (")
                
                arrangement, rest = ARRANGEMENT.parse(rest)
                
                rest = consume(rest, ")")
                arrangements.append(arrangement)
        except Exception as e:
            print(e)

        if OP == "ORR":
            return ORR(arrangements), rest
        else:
            return AND(arrangements), rest


class AND(BINOP):
    def __init__(self, arrangements):
        super().__init__(arrangements, "AND")

    @classmethod
    def parse(cls, string):
        return super().parse(string, "AND")

class ORR(BINOP):
    def __init__(self, arrangements):
        super().__init__(arrangements, "ORR")

    @classmethod
    def parse(cls, string):
        return super().parse(string, "ORR")


import sys
current_module = sys.modules[__name__]

x = BINOP.__subclasses__()[0]
print(x)