import math as m

list =[]

def calc_primes_up_to(max_value):
    for i in  range(2,max_value+1):
        for j in range(2,i//2):
            if(i % j == 0):
                continue
            else:
                list.append(i)


max_value = int(input("Enter the number upto which you want to get prime number: "))
calc_primes_up_to(max_value)
print(list)