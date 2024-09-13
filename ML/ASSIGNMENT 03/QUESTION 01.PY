import math as m



def calc_primes_up_to(max_value):
    primes = []
    for i in  range(2,max_value+1):
        is_prime = True
        for j in range(2,int(m.sqrt(i))+1):
            if(i % j == 0):
                is_prime = False
                break
        if(is_prime):
            primes.append(i)
    return primes


max_value = int(input("Enter the number upto which you want to get prime number: "))
print(calc_primes_up_to(max_value))