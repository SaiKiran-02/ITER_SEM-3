'''
#
Q 03 Write function gcd(a, b) that computes the greatest common divisor (GCD) recursively.
'''

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(18,24))

