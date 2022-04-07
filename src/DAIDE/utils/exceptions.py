__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"

class ParseError(Exception):
    def __init__(self, string, p_type):
        super().__init__("Can't parse \"" + string + "\" as " + p_type + ".")

class ConsumeError(ParseError):
    def __init__(self, string, to_consume):
        super().__init__(f"Can't consume {to_consume} from {string}.")