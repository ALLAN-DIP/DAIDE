__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"

from DAIDE.syntax.DAIDE_OBJECT import DAIDE_OBJECT
from DAIDE.utils.parsing import consume 

class ARRANGEMENT(DAIDE_OBJECT):
    """an ARRANGEMENT object"""
    
    def __init__(self, arrangement):
        self.arrangement = arrangement
    
    def __str__(self):
        return str(self.arrangement)

    @classmethod
    def parse(cls, string):
        print(string)
        if consume(string, "AND", False) != False:
            arrangement, rest = AND.parse(string)
        elif consume(string, "ORR", False) != False:
            arrangement, rest = ORR.parse(string)
        elif consume(string, "XDO", False) != False:
            arrangement, rest = XDO.parse(string)
        elif consume(string, "(", False) != False:
            arrangement, rest = ORDER.parse(string)

        return ARRANGEMENT(arrangement), rest