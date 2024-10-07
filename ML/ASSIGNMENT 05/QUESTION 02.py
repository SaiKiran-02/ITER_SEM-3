'''
#
Q 02 Write a Python program using a list that reads the integers between 1 and 100 and counts
the occurrences of each. Assume the input ends with 0.

     Here is a sample run of the program:
     Enter the integers between 1 and 100: 2 5 6 5 4 3 23 43 2 0
        2 occurs 2 times
        3 occurs 1 time
        4 occurs 1 time
        5 occurs 2 times
        6 occurs 1 time
        23 occurs 1 time
        43 occurs 1 time
'''
l = []
print("Enter 0 to end your inputs.")
while 1:
    try:
        item = int(input("Enter the integers between 1 to 100: "))
        if type(item) != 'int':
            l.append(item)
        if item == 0:
            break
        else:
            continue
    except Exception as e:
        print(e)
        print("Enter Integer numbers only.")

c = [l.count(item) for item in l]
s = []
for i in range(len(l)-1):
    if l[i] not in s:
        print(l[i]," occurs ",l.count(l[i])," times.")
        s.append(l[i])




