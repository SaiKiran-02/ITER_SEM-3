'''
#
Q 08 Write a Python program that randomly fills in 0s and 1s into a 4-by-4 matrix, prints the
     matrix, and finds the first row and column with the most 1s.

     Here is a sample run of the program:
        0 0 1 1
        0 0 1 1
        1 1 0 1
        1 0 1 0
        The largest row index: 2
        The largest column index: 2
'''
import random as r

l = []
for i in range(4):
    tem_l = []
    for j in range(4):
        item = r.randint(0,1)
        tem_l.append(item)
    l.append(tem_l)
mat = [print(i) for i in l]


# to be completed
