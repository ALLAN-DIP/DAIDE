from DAIDE import AND
from utils import EXAMPLE_ORDER, str_parse_str_test
inputs = [[EXAMPLE_ORDER, EXAMPLE_ORDER]]

for input in inputs:
    object = AND(input)
    str_parse_str_test(object, "SPS test failure")

