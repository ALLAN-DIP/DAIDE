__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"

from abc import ABC, abstractmethod

class DAIDE_OBJECT(ABC):
    """Abstract Base Class for DAIDE objects"""

    @abstractmethod
    def __str__(self):
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def parse(cls, str):
        raise NotImplementedError()