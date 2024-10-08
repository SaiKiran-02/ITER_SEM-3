'''
#
Q 06 Write function to_binary(n) that recursively converts the given positive integer into a
textual binary representation. No call to int(x, base) may be used.
'''
def to_binary(n):
    if n == 0:
        return ""
    else:
        return to_binary(n//2) + str(n%2)

n = 8
if n == 0:
    print('0')
else:
    print(to_binary(n))

