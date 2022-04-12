__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"

from DAIDE.core import DaideObject, Arrangement
from DAIDE.utils.parsing import consume, parse_with_parens

class PRP(DaideObject):
    """PRP (arrangement)"""
    def __init__(self, arrangement):
        self.arrangement = arrangement

    def __str__(self):
        return f"{str(self.__class__.__name__)} ({self.arrangement})"

    @classmethod
    def parse(cls, string):
        rest = consume(string, "PRP ")
        arrangement, rest = parse_with_parens(rest, Arrangement)
        return PRP(arrangement), rest
        