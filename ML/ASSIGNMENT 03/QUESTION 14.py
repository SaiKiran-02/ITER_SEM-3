import math as m

def sine(x):
    sineVal = x
    n = 3
    sign = -1
    term = 100

    while(abs(term)>1e-6):
        term = sign * (x**n)/m.factorial(n)
        sineVal +=term
        n +=2
        sign *=-1

    return sineVal

theta = m.pi/4
print(f"sin({theta: 0.4f}) = {sine(theta): 0.4f}")
print("Actual value = ",m.sin(theta))