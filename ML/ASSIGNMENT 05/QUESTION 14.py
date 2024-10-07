'''
#
Q 14 Write a program that prints up to nth Fibonacci number by using a dictionary.
'''
# using iteration
def febonacci(n):
    if n<= 0:
        return 0
    elif n == 1:
        return 1

    a = 0
    b = 1
    print(a,end=',')
    for i in range ( 2,n+1 ):
        print(b, end=",")
        a , b = b , a+b
    return b

# using dictionary
def fibonacci_dict(n):
    fib_dict = {0: 0, 1: 1}
    for i in range(2, n + 1):
        fib_dict[i] = fib_dict[i-1] + fib_dict[i-2]
    for i in range(n + 1):
        print(fib_dict[i],end=",")


n = 10
print(febonacci(n))
fibonacci_dict(n)

