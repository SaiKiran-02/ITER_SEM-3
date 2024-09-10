import math

tuple = eval(input("Enter 3 numbers: "))
sum =0
for i in tuple:
    sum = sum+i

min = min(tuple[0],tuple[1],tuple[2])
max = max(tuple[0],tuple[1],tuple[2])
mid = sum - (min+max)

list = [min,mid,max]
print(f"numbers are sorted in accending order: {list}")
