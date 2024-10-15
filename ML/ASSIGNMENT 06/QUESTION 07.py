'''
#
Q 07 Write conversions to octal and hexadecimal numbers by implementing the corresponding
     functions to_octal(n) and to_hex(n). Again, no call to int(x, base) may be used.
'''

def to_hex(n):
    if n == 0:
        return "0"

    hex_digits = []
    n = abs(n)

    while n > 0:
        remainder = n % 16
        hex_digits.append(str(remainder) if remainder < 10 else chr(remainder - 10 + ord('A')))
        n //= 16

    return ''.join(hex_digits[::-1])

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

