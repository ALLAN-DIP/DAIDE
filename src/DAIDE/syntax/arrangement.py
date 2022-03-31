__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"

from DAIDE.syntax.daide_object import DAIDE_OBJECT
from DAIDE.utils.parsing import consume
from DAIDE.syntax.lvl0.order import ORDER 

class ARRANGEMENT(DAIDE_OBJECT):
    """an ARRANGEMENT object"""
    
    def __init__(self, arrangement):
        self.arrangement = arrangement
    
    def __str__(self):
        return str(self.arrangement)

    @classmethod
    def parse(cls, string):
        no_sub_parse = ["ARRANGEMENT", "ORDER"]
        for subclass in DAIDE_OBJECT.__subclasses__():
            if subclass.__name__ not in no_sub_parse:
                if consume(string, subclass.__name__, False) != False:
                    arrangement, rest = subclass.parse(string)
        else:
            arrangement, rest = ORDER.parse(string)

        return ARRANGEMENT(arrangement), rest
