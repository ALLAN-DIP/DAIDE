__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"

from DAIDE.syntax.daide_object import DAIDE_OBJECT
from DAIDE.syntax.arrangement import ARRANGEMENT
from DAIDE.utils.parsing import consume 

class RESPONSE(DAIDE_OBJECT):
    """YES, REJ, stuff like that"""
    def __init__(self, string, response):
        self.string = string
        self.response = response

    def __str__(self):
        return str(self.response) + " (" + self.msg + ")"

    @classmethod
    def parse(cls, string):
        response = string[:3]
        rest = string[3:]
        rest = consume(" (")
        arrangement, rest = ARRANGEMENT.parse(rest)
        rest = consume(")")

        for subclass in RESPONSE.__subclasses__():
            if subclass.__name__ == response:
                return subclass(arrangement), rest

class YES(RESPONSE):
    pass

class HUH(RESPONSE):
    pass