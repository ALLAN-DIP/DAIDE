__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"

from abc import ABC

from DAIDE.syntax.daide_object import DAIDE_OBJECT
from DAIDE.syntax.arrangement import ARRANGEMENT
from DAIDE.utils.parsing import consume 
from DAIDE.utils.exceptions import ConsumeError

class BINOP(DAIDE_OBJECT, ABC):
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
        try:
            while True:
                rest = consume(rest, " (")
                
                arrangement, rest = ARRANGEMENT.parse(rest)
                
                rest = consume(rest, ")")
                arrangements.append(arrangement)
        except ConsumeError as e:
            pass

        for subclass in BINOP.__subclasses__():
            if subclass.__name__ == OP:
                return subclass(arrangements)


class AND(BINOP):
    def __init__(self, arrangements):
        super().__init__(arrangements)
    
    def __str__(self):
        return super().__str__()


class ORR(BINOP):
    def __init__(self, arrangements):
        super().__init__(arrangements)

    def __str__(self):
        return super().__str__()

if __name__ == "__main__":
    import sys
    current_module = sys.modules[__name__]

    x = BINOP.__subclasses__()[0]
    print("-")
    print()