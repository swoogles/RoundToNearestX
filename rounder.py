# Test data defined in assignment
# This is stored in unorderd maps, since I don't feel that the order of testing 
# is significant.
values50 = {
    54:50,
    75:100,
    98:100,
    119:100,
    }

values22 = {
    22:22,
    29:22,
    33:44,
    47:44,
    }

fullData = {
    50: values50,
    22: values22,
    }

""" 
Return number rounded to nearest multiple of base

Per the assignment:If the result is 0, return the base, as it will have to be 
the next closest multiple.

Arguments:
startNum -- Number to be rounded
base -- Base to determine rounding values
"""
def round_to_base(startNum, base):
    assert base > 0, "Invalid base for rounding"
    # Left side of the decimal point is the number of times the base
    # can be divided into the number.
    # Right hand side determines whether you will go up or down for
    # nearest multiple.
    firstDiv = (float(startNum)/base)

    result = int(base * round(firstDiv))
    if result == 0:
        result = base
    return result


# Iterate through maps of test data with corresponding base
for base, testData in fullData.items():
    # num is the starting value
    # roundedTarget is what it should be rounded to
    for num, roundedTarget in testData.items():
        roundedActual = round_to_base(num, base)
        assert roundedTarget == roundedActual, (
            "Expected: %r Got: %r" % (roundedTarget, roundedActual))
        print("Number: ", num, " Rounded: ", roundedTarget)
