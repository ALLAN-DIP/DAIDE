

__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"

from functools import reduce
import re

import DAIDE.config as config
from DAIDE.core import DaideObject
from DAIDE.utils.parsing import consume 
from DAIDE.utils.exceptions import ParseError 
from DAIDE.syntax.lvl0.unit import Unit
from DAIDE.syntax.lvl0.province import Province

class ALY(DaideObject):
    def __init__(self, allies, opponenents) -> None:
        self.allies = allies
        self.opponenents = opponenents

    def __str__(self):
        allies_str = reduce(lambda s, a: f"{s} " + str(a), self.allies)
        opponents_str = reduce(lambda s, a: f"{s} " + str(a), self.opponenents)
        return f"ALY ({allies_str}) VSS ({opponents_str})"

    @classmethod
    def parse(self, string):
        groups = re.findall(r'\(([a-zA-Z\s]*)\)', string)

        if len(groups) != 2:
            more = len(groups) > 2
            raise ParseError("Found " + "more" if more else "less"  + " 2 groups", "ALY")

        rest = consume(string, "ALY (")

        allies = groups[0].split(" ")
        opponents = groups[1].split(" ")

        rest = consume(rest, groups[0])
        rest = consume(rest, ") VSS (")
        rest = consume(rest, groups[1])
        rest = consume(rest, ")")

        if allies and opponents:
            return ALY(allies, opponents), rest
        else:
            raise ParseError("A minimum of 2 powers are needed for an alliance")
        
if __name__ == "__main__":
    x = ALY(["FFF", "FFF"], ["FFF", "FFF"])
    print(ALY.parse(str(x)))