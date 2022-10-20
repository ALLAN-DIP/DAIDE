__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"

from DAIDE.core import SimpleParensObject, Arrangement
from DAIDE.utils.parsing import consume, parse_with_parens

class Response(SimpleParensObject):
    """YES, REJ, stuff like that"""

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
    pass

class HUH(Response):
    pass

class REJ(Response):
    pass
