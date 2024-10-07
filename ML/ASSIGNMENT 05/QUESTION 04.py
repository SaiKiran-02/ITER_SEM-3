'''
#
Q 04 Define a function that eliminates the duplicate values in the list. Write a Python program
     that reads in ten integers, invokes the method, and displays the result.

     Here is the sample run of the program:
     Enter ten numbers: 1 2 3 2 1 6 3 4 5 2
'''

def eliminate_duplicate(l):
    new_l = []
    for i in l:
        if i not in new_l :
            new_l.append(i)
    return new_l


print("Enter 10 Integer values: ")
l = []
for i in range(10):
    try:
        item = int(input("Enetr number: "))
        l.append(item)
    except ValueError:
        print(ValueError)
        print("Enter Integer values only. ")
new_l = eliminate_duplicate(l)
print(new_l)
