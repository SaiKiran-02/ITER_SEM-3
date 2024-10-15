'''
#
Q 04 Write function lcm(a, b) that computes the lowest common multiplier (LCM)
     recursively.
'''

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

print(lcm(4,5))