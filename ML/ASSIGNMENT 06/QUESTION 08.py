'''
#
Q 08 Write recursive function power_of(value, exponent) that exponentiates the given
     positive integer with the positive number specified as second parameter.
     For example, the call power_of(4, 2) should return the square of 4, so it computes

     2^4 = 16. You may not use the built-in functionality pow() or the operator **.
'''

def power_of(b , p):
    if b == 1 or p == 0:
        return 1
    if b == 0:
        return 0
    else:
        return b * power_of(b , p-1)

print(power_of(2,10))