import math

for i in range(1,501):
    sum = 0
    for j in range(1,i):
        if(i % j == 0):
            sum+=j
    if(sum == i ):
        print(f"{i} is a perfect number")
