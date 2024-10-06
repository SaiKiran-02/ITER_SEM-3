'''
#
Q 03 Write a function that finds the smallest element in a list of double values. Write a Python
     program that prompts the user to enter ten numbers, invokes this function to return the
     minimum value, and displays the minimum value.

     Here is a sample run of the program:
     Enter ten numbers: 1.9 2.5 3.7 2 1.5 6 3 4 5 2
     The minimum number is: 1.5
'''


def smallest_element(l):
    return min(l)

print("Enter 10 numbers: ")
l =[]
for i in range(10):
    item = float(input("Enter number: "))
    l.append(item)
min = smallest_element(l)
print(f"minimun of {l} is {min}")

