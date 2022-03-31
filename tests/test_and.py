from DAIDE import AND

inputs = [[], ["FFF FFF FFF"], ["FFF FFF FFF", "GGG GGG GGG"]]

for input in inputs:
    object = AND(input)
    print(AND(str(AND(input))))
    # assert str(AND(input)) == str(AND(str(AND(input)))), "PBT fail"

