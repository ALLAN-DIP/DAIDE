__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"

from functools import reduce
import re

import DAIDE.config as config
from DAIDE.core import DaideObject
from DAIDE.utils.parsing import consume 
from DAIDE.utils.exceptions import ParseError 
from DAIDE.syntax.lvl0.unit import Unit
from DAIDE.syntax.lvl0.province import Province

class Order(DaideObject):
    """(unit) order_type"""
    def __init__(self, unit, order_type, non_DAIDE_order=None):
        self.unit = unit
        self.order_type = order_type
        self.non_DAIDE_order = non_DAIDE_order

    def __str__(self):
        if self.non_DAIDE_order:
            return str(self.non_DAIDE_order)
        return f"({str(self.unit)}) {str(self.order_type)}"

    @classmethod
    def parse(cls, string):
        if not config.ORDERS_DAIDE:
            regex = re.compile("^([^\(\)]*)")
            match = regex.match(string)
            if match:
                order = match.group()
                rest = string[len(order):]

            return Order(None, None, non_DAIDE_order=order), rest
                
        unit, rest = Unit.parse(string, True)
        
        rest = consume(rest, " ")
        
        for subclass in Order.__subclasses__():
            # print(subclass.__name__, rest)
            # print(consume(rest, subclass.__name__, False))
            if consume(rest, subclass.__name__, False) != False:
                # print("HERE")
                order_type, rest = subclass.parse(rest)
                break
        else:
            raise ParseError(string, "Order")

        return Order(unit, order_type), rest


class HLD(Order):
    """
    (unit) HLD
    
    e.g. (ENG AMY LVP) HLD
    """
    def __init__(self):
        pass

    def __str__(self):
        return "HLD"

    @classmethod
    def parse(cls, string):
        rest = consume(string, "HLD")
        return HLD(), rest
                
class MTO(Order):
    
    regex = re.compile("^(ADR|AEG|ALB|ANK|APU|ARM|BAL|BAR|BEL|BER|BLA|BOH|BRE|BUD|BUL|BUR|CLY|CON|DEN|EAS|ECH|EDI|FIN|GAL|GAS|GOB|GOL|GRE|HEL|HOL|ION|IRI|KIE|LON|LVN|LVP|MAO|MAR|MOS|MUN|NAF|NAO|NAP|NTH|NWG|NWY|PAR|PIC|PIE|POR|PRU|ROM|RUH|RUM|SER|SEV|SIL|SKA|SMY|SPA|STP|SWE|SYR|TRI|TUN|TUS|TYR|TYS|UKR|VEN|VIE|WAL|WAR|WES|YOR)")
    
    def __init__(self, province):
        """MTO province"""
        self.province = province

    def __str__(self):
        return "MTO " + str(self.province)

    @classmethod
    def parse(cls, string):
        rest = consume(string, "MTO ")
        match = cls.regex.match(rest)
        if match:
            province = match.group()
            rest = rest[len(province):]
        else:
            raise ParseError(string, "MTO")

        return MTO(province), rest

class SUP(Order):
    def __init__(self, unit, mto_order=None):
        """SUP (unit) **OR** SUP (unit) MTO prov_no_coast"""
        self.unit = unit
        self.mto_order = mto_order
    
    def __str__(self):
        return f"SUP ({str(self.unit)})" + (" " + str(self.mto_order) if self.mto_order else "")

    @classmethod
    def parse(cls, string):
        rest = consume(string, "SUP ")
        unit, rest = Unit.parse(rest, parens=True)
        
        mto = None
        if rest[:4] == " MTO":
            rest = consume(rest, " ")
            mto, rest = MTO.parse(rest)

        return SUP(unit, mto), rest

class CVY(Order):
    def __init__(self, unit, cto_order):
        """CVY (unit) CTO province"""
        self.unit = unit
        self.cto_order = cto_order
    
    def __str__(self):
        return f"CVY ({str(self.unit)})" + (" " + str(self.cto_order) if self.cto_order else "")

    @classmethod
    def parse(cls, string):
        rest = consume(string, "CVY ")
        unit, rest = Unit.parse(rest, parens=True)
        cto = None
        if rest[:4] == " CTO":
            rest = consume(rest, " ")
            cto, rest = CTO.parse(rest)

        return CVY(unit, cto), rest

class CTO(Order):
    def __init__(self, province, via_order=None):
        """CTO province VIA (sea_province sea_province ...)"""
        self.province = province
        self.via_order = via_order
    
    def __str__(self):
        return f"CTO {str(self.province)}" + (" " + str(self.via_order) if self.via_order else "")

    @classmethod
    def parse(cls, string):
        rest = consume(string, "CTO ")
        province, rest = Province.parse(rest)
        via = None
        if rest[:4] == " VIA":
            rest = consume(rest, " ")
            via, rest = VIA.parse(rest)

        return CTO(province, via), rest

class VIA(Order):
    def __init__(self, provinces):
        self.provinces = provinces
    
    def __str__(self):
        return "VIA (" + reduce(lambda s, a: f"{s} " + str(a), self.provinces) + ")"

    @classmethod
    def parse(cls, string):
        rest = consume(string, "VIA (")
        provinces = []
        province1, rest = Province.parse(rest)
        provinces.append(province1)
        while rest[0] == " ":
            rest = consume(rest, " ")
            province, rest = Province.parse(rest)
            provinces.append(province)

        rest = consume(rest, ")")

        return VIA(provinces), rest