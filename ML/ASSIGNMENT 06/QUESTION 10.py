'''
#
Q 10 Write a recursive function harmonic_sum(n) to calculate the harmonic sum of first n
     terms.
     Note: The harmonic sum is the sum of reciprocals of the positive integers. For example, if
     n = 4, the output should be (1+1/2+1/3+1/4 ) = 2.0833
'''

def harmonic_sum(n):
    if n == 1:
        return 1.0
    else:
        return 1/n + harmonic_sum(n - 1)
n = 4
result = harmonic_sum(n)
print(f"The harmonic sum of the first {n} terms is: {result:.4f}")