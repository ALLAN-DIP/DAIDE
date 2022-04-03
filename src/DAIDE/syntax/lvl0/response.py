__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"

from DAIDE.core import Arrangement
from DAIDE.utils.parsing import consume, parse_with_parens

class Response(Arrangement):
    """YES, REJ, stuff like that"""
    def __init__(self, arrangement):
        self.arrangement = arrangement

    def __str__(self):
        return f"{str(self.__class__.__name__)} ({self.arrangement})"

    @classmethod
    def parse(cls, string):
        response = string[:3]
        rest = string[3:]
        rest = consume(rest, " ")
        arrangement, rest = parse_with_parens(rest, Arrangement)

        for subclass in Response.__subclasses__():
            if subclass.__name__ == response:
                return subclass(arrangement), rest

class YES(Response):
    # def __init__(self, string):
    #     super
    pass
class HUH(Response):
    pass