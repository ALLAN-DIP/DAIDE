"""Property base testing"""

from DAIDE import UNIT, ORDER, HLD

EXAMPLE_UNIT = UNIT("FFF FFF FFF")
EXAMPLE_ORDER = ORDER(EXAMPLE_UNIT, HLD())

def str_parse_str_test(arrangement, error_msg):
    """
    A property base test which ensures that
    the str of an object is equivalent to 
    parsing that str then converting it back to str
    """
    s = str(arrangement)
    assert s == str(type(arrangement).parse(s)), error_msg