# DAIDE

SUPPORTS most bot communication commands levels 0-30

This library parses DAIDE strings into a recursive object model. It can also generate a string from the object model.

e.g. `"AND (order1) (order2)" -> AND([order1, order2])`

## Usage

(FFF are placeholders)

```python
>>> from DAIDE import DAIDE_parse
>>> arrangement = DAIDE_parse('AND (XDO ((FFF FFF FFF) HLD)) (XDO ((FFF FFF FFF) HLD))')

# ARRANGEMENT is wrapper object around all parsed DAIDE objects
>>> arrangement
<DAIDE.syntax.arrangement.ARRANGEMENT object at 0x7fbd43285470>

# parsed objects are nested
>>> arrangement.arrangement
<DAIDE.syntax.lvl30.binop.AND object at 0x7f8fabb332e8>
>>> arrangement.arrangement.arrangements
[<DAIDE.syntax.arrangement.ARRANGEMENT object at 0x7f8fab9bd588>, <DAIDE.syntax.arrangement.ARRANGEMENT object at 0x7f8fab9bd630>]

# generate string from DAIDE object
>>> str(arrangement)
'AND (XDO ((FFF FFF FFF) HLD)) (XDO ((FFF FFF FFF) HLD))'

# easily compose DAIDE keywords
>>> from DAIDE import ORR, ORDER, UNIT, HLD
>>> arrangement = ORR([ORDER(UNIT("FFF FFF FFF"), HLD()), ORDER(UNIT("FFF FFF FFF"), HLD())])
>>> str(arrangement)
<DAIDE.syntax.lvl30.binop.ORR object at 0x7f8fabb33dd8>
```

## Installation

### From Github (easiest)

`pip install git+https://github.com/trigaten/DAIDE.git`

### From inside repo

`pip install -e .`

## Adding Syntax

All syntax words are represented as objects which implement 

a `parse()` function and `__str__`




