'''
#
Q 07 Write conversions to octal and hexadecimal numbers by implementing the corresponding
     functions to_octal(n) and to_hex(n). Again, no call to int(x, base) may be used.
'''

def to_hexadecimal(n):
    
def to_octal(n):
    if n == 0:
        return ""
    else:
        return to_octal(n//8) + str(n%8)

n = 11
if n == 0:
    print('0')
else:
    print(to_octal(n))

