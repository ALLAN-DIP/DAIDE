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