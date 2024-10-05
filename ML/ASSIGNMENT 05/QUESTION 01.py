'''
#
Q 01 Write a Python program to create a list of integers of size N and store random values in
     it. Find and display the sum and average. Create two more lists that contain the even
     and odd values from this list.
'''
import random as r
def list_sum(l):
    sum = 0
    for i in l:
        sum += i
    return sum

def list_avg(l):
    return sum(l)/len(l)

def list_split(l):
    even = []
    odd = []
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even , odd

N = int(input("Enter size of list: "))
l = []
for i in range(N):
    item = r.randint(1,101)
    l.append(item)

print(list_sum(l))
print(list_avg(l))
print(list_split(l))

