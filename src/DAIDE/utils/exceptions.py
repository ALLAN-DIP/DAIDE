__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"

class ParseError(Exception):
    def __init__(self, string, p_type):
        super().__init__("Can't parse \"" + string + "\" as " + p_type + ".")
