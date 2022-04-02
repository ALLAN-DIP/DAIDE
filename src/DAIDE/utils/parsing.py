__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"

from DAIDE.utils.exceptions import ParseError, ConsumeError

def consume(string, sub, error=True):
    """"""
    len_sub = len(sub)
    if string[:len_sub] == sub:
        return string[len_sub:]
    else:
        if error:
            raise ConsumeError(string, f"Consume \"{sub}\"")
        else:
            return False

def parse_with_parens(string, _class):
    rest = consume(string, "(")
        
    parsed_class, rest = _class.parse(rest)

    rest = consume(rest, ")")

    return parsed_class, rest