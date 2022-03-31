__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"

import re

from DAIDE.syntax.DAIDE_OBJECT import DAIDE_OBJECT

class PROVINCE(DAIDE_OBJECT):
    regex = re.compile("^(ADR|AEG|ALB|ANK|APU|ARM|BAL|BAR|BEL|BER|BLA|BOH|BRE|BUD|BUL|BUR|CLY|CON|DEN|EAS|ECH|EDI|FIN|GAL|GAS|GOB|GOL|GRE|HEL|HOL|ION|IRI|KIE|LON|LVN|LVP|MAO|MAR|MOS|MUN|NAF|NAO|NAP|NTH|NWG|NWY|PAR|PIC|PIE|POR|PRU|ROM|RUH|RUM|SER|SEV|SIL|SKA|SMY|SPA|STP|SWE|SYR|TRI|TUN|TUS|TYR|TYS|UKR|VEN|VIE|WAL|WAR|WES|YOR)")

    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    @classmethod
    def parse(cls, string):
        """Parse PROVINCE"""

        match = cls.regex.match(string)
        if match:
            matched_string = match.group()
            province = PROVINCE(matched_string)
            rest = string[len(matched_string):]

            return province, rest
        else:
            raise ParseError(string, "PROVINCE")