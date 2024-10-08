'''
#
Q 02 Calculate the sum of the digits of a number recursively. Write recursive function calc_
     sum_of_digits(value) for this purpose.
'''

def calc_sum_of_digits(n):
    sum = 0
    if n >= 0 and n <=9:
        return n
    else:
        return sum + n%10 + calc_sum_of_digits(n//10)

print(calc_sum_of_digits(92))