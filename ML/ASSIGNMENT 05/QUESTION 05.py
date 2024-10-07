'''
#
Q 05 Define a function that returns the sum of all the elements in a specified column in a
     matrix. Write a Python program that reads a 3-by-4 matrix and displays the sum of each
     column.

     Here is a sample run:
     Enter a 3-by-4 matrix row by row:
     1.5 2 3 4
     5.5 6 7 8
     9.5 1 3 1
     Sum of the elements at column 0 is 16.5
     Sum of the elements at column 1 is 9.0
     Sum of the elements at column 2 is 13.0
     Sum of the elements at column 3 is 13.0
'''

l = []
for i in range(1,4):
    tem_l = []
    for j in range(4):
        item = float(input(f"Enter {i} row element: "))
        tem_l.append(item)
    l.append(tem_l)

mat = [print(i) for i in l]


for i in range(4):
    sum = 0
    for j in range(3):
        sum += l[j][i]
    print(f"Sum of the elements at column {i} is {sum}")

