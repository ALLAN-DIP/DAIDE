
from DAIDE import UNIT, ORDER, PROVINCE, ARRANGEMENT
from DAIDE import MTO, SUP, CVY, CTO, VIA
from DAIDE import XDO
from DAIDE import AND, ORR
from utils import EXAMPLE_ORDER, EXAMPLE_UNIT, EXAMPLE_PROVINCE, str_parse_str_test


"""lvl0"""

object = EXAMPLE_PROVINCE
str_parse_str_test(object)

object = EXAMPLE_UNIT
str_parse_str_test(object)

# orders
object = EXAMPLE_ORDER
str_parse_str_test(object)

object = ORDER(EXAMPLE_UNIT, MTO(EXAMPLE_PROVINCE))
str_parse_str_test(object)

object = ORDER(EXAMPLE_UNIT, SUP(EXAMPLE_UNIT))
str_parse_str_test(object)

object = ORDER(EXAMPLE_UNIT, SUP(EXAMPLE_UNIT, MTO(EXAMPLE_PROVINCE)))
str_parse_str_test(object)

object = ORDER(EXAMPLE_UNIT, CVY(EXAMPLE_UNIT, CTO(EXAMPLE_PROVINCE)))
str_parse_str_test(object)

object = ORDER(EXAMPLE_UNIT, CTO(EXAMPLE_PROVINCE, VIA([EXAMPLE_PROVINCE, EXAMPLE_PROVINCE])))
str_parse_str_test(object)

"""lvl20"""
object = XDO(EXAMPLE_ORDER)
str_parse_str_test(object)


"""lvl30"""
object = AND([EXAMPLE_ORDER, EXAMPLE_ORDER])
str_parse_str_test(object)

object = ORR([EXAMPLE_ORDER, EXAMPLE_ORDER])
str_parse_str_test(object)

object = ARRANGEMENT(AND([XDO(EXAMPLE_ORDER), XDO(EXAMPLE_ORDER)]))
str_parse_str_test(object)
