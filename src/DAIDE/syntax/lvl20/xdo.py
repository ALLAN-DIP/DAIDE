__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"

from DAIDE.syntax.daide_object import DAIDE_OBJECT
from DAIDE.syntax.lvl0.order import ORDER 
from DAIDE.utils.parsing import consume 

class XDO(DAIDE_OBJECT):

    def __init__(self, order):
        self.order = order

    def __str__(self):
        return f"XDO ({str(self.order)})"

    @classmethod
    def parse(cls, string):
        """Parse XDO"""

        rest = consume(string, "XDO (")
        
        order, rest = ORDER.parse(rest)

        rest = consume(rest, ")")
        
        return XDO(order), rest