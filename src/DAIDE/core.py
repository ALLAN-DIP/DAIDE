from DAIDE.syntax.arrangement import ARRANGEMENT
from DAIDE.utils.parsing import ParseError

def DAIDE_parse(string):
    arrangement, rest = ARRANGEMENT.parse(string)
    if rest != "":
        raise ParseError("Couldnt completely parse string")
    return arrangement