__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"

from abc import ABC, abstractmethod
from DAIDE.utils.parsing import ParseError
from DAIDE.utils.parsing import consume

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
        from DAIDE.syntax.lvl20.xdo import XDO
        from DAIDE.syntax.lvl30.binop import Binop
        from DAIDE.syntax.lvl0.order import Order 
        from DAIDE.syntax.lvl0.response import Response
        subclasses = Response.__subclasses__() + Binop.__subclasses__() + [XDO]
        for subclass in subclasses:
            if consume(string, subclass.__name__, False) != False:
                arrangement, rest = subclass.parse(string)
                break
        else:
            arrangement, rest = Order.parse(string)

        return arrangement, rest
        
def parse(string):
    object, rest = DaideObject.parse(string)

    if rest != "":
        raise ParseError("Couldnt completely parse string")
    return object