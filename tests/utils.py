"""Property base testing"""

from DAIDE import Unit, Order, HLD
from DAIDE import Province

EXAMPLE_UNIT = Unit("FFF FFF FFF")
EXAMPLE_ORDER = Order(EXAMPLE_UNIT, HLD())
EXAMPLE_PROVINCE = Province("ADR")

def str_parse_str_test(arrangement):
    """
    A property base test which ensures that
    the str of an object is equivalent to 
    parsing that str then converting it back to str
    """
    s = str(arrangement)
    o, r = type(arrangement).parse(s)
    assert r == "", "not everything parsed: " + r
    print(s, str(o))
    assert s == str(o), f"{arrangement.__class__.__name__} SPS test failed: \n" + s + "\n" + str(o)