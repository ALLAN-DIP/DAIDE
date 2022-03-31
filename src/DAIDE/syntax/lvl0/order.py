__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"

from functools import reduce
import re

from DAIDE.syntax.daide_object import DAIDE_OBJECT
from DAIDE.utils.parsing import consume 
from DAIDE.utils.exceptions import ParseError 
from DAIDE.syntax.lvl0.unit import UNIT
from DAIDE.syntax.lvl0.province import PROVINCE

class ORDER(DAIDE_OBJECT):
    def __init__(self, unit, order_type):
        self.unit = unit
        self.order_type = order_type

    def __str__(self):
        return f"({str(self.unit)}) {str(self.order_type)}"

    @classmethod
    def parse(cls, string):
        unit, rest = UNIT.parse(string, True)
        
        rest = consume(rest, " ")
        
        for subclass in ORDER.__subclasses__():
            if consume(rest, subclass.__name__, False) != False:
                order_type, rest = subclass.parse(rest)
        
        return ORDER(unit, order_type), rest


class HLD(ORDER):
    def __init__(self):
        pass

    def __str__(self):
        return "HLD"

    @classmethod
    def parse(cls, string):
        rest = consume(string, "HLD")
        return HLD(), rest
                
class MTO(ORDER):
    
    regex = re.compile("^(ADR|AEG|ALB|ANK|APU|ARM|BAL|BAR|BEL|BER|BLA|BOH|BRE|BUD|BUL|BUR|CLY|CON|DEN|EAS|ECH|EDI|FIN|GAL|GAS|GOB|GOL|GRE|HEL|HOL|ION|IRI|KIE|LON|LVN|LVP|MAO|MAR|MOS|MUN|NAF|NAO|NAP|NTH|NWG|NWY|PAR|PIC|PIE|POR|PRU|ROM|RUH|RUM|SER|SEV|SIL|SKA|SMY|SPA|STP|SWE|SYR|TRI|TUN|TUS|TYR|TYS|UKR|VEN|VIE|WAL|WAR|WES|YOR)")
    
    def __init__(self, province):
        """MTO province"""
        self.province = province

    def __str__(self):
        return "MTO " + self.province

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

class SUP(ORDER):
    def __init__(self, unit, mto_order):
        """SUP (unit) **OR** SUP (unit) MTO prov_no_coast"""
        self.unit = unit
        self.mto_order = mto_order
    
    def __str__(self):
        return "SUP " + str(self.unit) + " " + str(self.mto_order) if self.mto_order else ""

    @classmethod
    def parse(cls, string):
        rest = consume(string, "SUP ")
        unit, rest = UNIT.parse(rest, parens=True)
        rest = consume(rest, " ")
        mto = None
        if rest[:3] == "MTO":
            mto, rest = MTO.parse(rest)

        return SUP(unit, mto), rest

class CVY(ORDER):
    def __init__(self, unit, cto_order):
        """CVY (unit) CTO province"""
        self.unit = unit
        self.cto_order = cto_order
    
    def __str__(self):
        return "CVY " + str(self.unit) + str(self.cto_order) if self.cto_order else ""

    @classmethod
    def parse(cls, string):
        rest = consume(string, "CVY ")
        unit, rest = UNIT.parse(rest, parens=True)
        rest = consume(rest, " ")
        cto = None
        if rest[:3] == "CTO":
            cto, rest = CTO.parse(rest)

        return CVY(unit, cto), rest

class CTO(ORDER):
    def __init__(self, province, via_order):
        """CTO province VIA (sea_province sea_province ...)"""
        self.province = province
        self.via_order = via_order
    
    def __str__(self):
        return "CTO " + str(self.unit) + str(self.via_order) if self.via_order else ""

    @classmethod
    def parse(cls, string):
        rest = consume(string, "CTO ")
        province, rest = PROVINCE.parse(rest, parens=True)
        rest = consume(rest, " ")
        via = None
        if rest[:3] == "VIA":
            via, rest = VIA.parse(rest)

        return CTO(province, via), rest

class VIA(ORDER):
    def __init__(self, provinces):
        self.provinces = provinces
    
    def __str__(self):
        return "VIA (" + reduce(lambda s, a: f"{s}, " + a, self.provinces) + ")"

    @classmethod
    def parse(cls, string):
        rest = consume(string, "VIA (")
        provinces = []
        province1, rest = PROVINCE.parse(rest)
        provinces.append(province1)
        while rest[0] == " ":
            rest = consume(rest, " ")
            province, rest = PROVINCE.parse(rest)
            provinces.append(province)

        
        provinces, rest = PROVINCE.parse(rest)
        rest = consume(rest, ")")

        return VIA(provinces), rest