__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"

from DAIDE.syntax.DAIDE_OBJECT import DAIDE_OBJECT
from DAIDE.utils.parsing import consume 

class XDO(DAIDE_OBJECT):

    def __init__(self, order):
        self.order = order

    def __str__(self):
        return str(self.order)

    @classmethod
    def parse(cls, string):
        """Parse XDO"""

        rest = consume(string, "XDO ")
        print("rest", rest)
        order, rest = ORDER.parse(rest)
        print("rest", rest)
        return XDO(order), rest