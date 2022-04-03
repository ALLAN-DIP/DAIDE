__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"

from DAIDE.core import Arrangement
from DAIDE.syntax.lvl0.order import Order 
from DAIDE.utils.parsing import consume, parse_with_parens

class XDO(Arrangement):

    def __init__(self, order):
        self.order = order

    def __str__(self):
        return f"XDO ({str(self.order)})"

    @classmethod
    def parse(cls, string):
        """Parse XDO"""

        rest = consume(string, "XDO ")
        
        order, rest = parse_with_parens(rest, Order)

        return XDO(order), rest