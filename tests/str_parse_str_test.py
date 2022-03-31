from DAIDE import AND, ORR
from DAIDE import UNIT, ORDER
from utils import EXAMPLE_ORDER, EXAMPLE_UNIT, str_parse_str_test

object = EXAMPLE_ORDER
str_parse_str_test(object, "ORDER SPS test failure")

object = EXAMPLE_UNIT
str_parse_str_test(object, "UNIT SPS test failure")

object = AND([EXAMPLE_ORDER, EXAMPLE_ORDER])
str_parse_str_test(object, "AND SPS test failure")

object = ORR([EXAMPLE_ORDER, EXAMPLE_ORDER])
str_parse_str_test(object, "ORR SPS test failure")

