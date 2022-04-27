__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"

from abc import ABC, abstractmethod
import DAIDE.utils.parsing as parsing
from DAIDE.utils.parsing import consume, parse_with_parens

class DaideObject(ABC):
    """Abstract Base Class for DAIDE objects"""

    @abstractmethod
    def __str__(self):
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def parse(cls, str):
        return Arrangement.parse(str)

class Arrangement(DaideObject, ABC):
    
    @abstractmethod
    def __str__(self):
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def parse(cls, string):
        from DAIDE.syntax.lvl0.order import Order 
        from DAIDE.syntax.lvl0.response import Response
        from DAIDE.syntax.lvl10.statement import FCT
        from DAIDE.syntax.lvl20.xdo import XDO
        from DAIDE.syntax.lvl30.binop import Binop
        
        
        subclasses = Response.__subclasses__() + Binop.__subclasses__() + [XDO,FCT]
        for subclass in subclasses:
            if consume(string, subclass.__name__, False) != False:
                arrangement, rest = subclass.parse(string)
                break
        else:
            arrangement, rest = Order.parse(string)

        return arrangement, rest

class SimpleParensObject(DaideObject):
    """
    Parsing class for classes that use simple parentheses + arrangement syntax
    e.g. YES (arrangement), PRP (arrangement)
    """
    def __init__(self, arrangement):
        self.arrangement = arrangement

    def __str__(self):
        return f"{str(self.__class__.__name__)} ({self.arrangement})"

    @classmethod
    def parse(cls, string):
        rest = consume(string, cls.__name__ + " ")
        arrangement, rest = parse_with_parens(rest, Arrangement)
        return cls(arrangement), rest
        
def parse(string):
    object, rest = DaideObject.parse(string)

    if rest != "":
        raise parsing.ParseError("Couldnt completely parse string")
    return object
