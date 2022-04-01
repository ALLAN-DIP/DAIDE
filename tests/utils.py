"""Property base testing"""

from DAIDE import UNIT, ORDER, HLD
from DAIDE import PROVINCE

EXAMPLE_UNIT = UNIT("FFF FFF FFF")
EXAMPLE_ORDER = ORDER(EXAMPLE_UNIT, HLD())
EXAMPLE_PROVINCE = PROVINCE("ADR")

def str_parse_str_test(arrangement):
    """
    A property base test which ensures that
    the str of an object is equivalent to 
    parsing that str then converting it back to str
    """
    s = str(arrangement)
    o, r = type(arrangement).parse(s)
    assert r == "", "not everything parsed"
    assert s == str(o), f"{arrangement.__class__.__name__} SPS test failed"