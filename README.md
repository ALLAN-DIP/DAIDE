# DAIDE

This library parses DAIDE strings into a recursive object model

e.g. `"AND (order1) (order2)" -> AND([order1, order2])`

It can also generate a string from the object model.

** Examples **

FFF are placeholders

`"AND (XDO ((FFF FFF FFF) HLD)) (XDO ((FFF FFF FFF) HLD))" -> AND([XDO(FFF FFF FFF), XDO(FFF FFF FFF))    `


## Installation

### From Github (easiest)

`pip install git+https://github.com/trigaten/DAIDE.git`

### From inside repo

`pip install -e .`

## Adding Syntax

All syntax words are represented as objects which implement 

a `parse()` function and `__str__`




