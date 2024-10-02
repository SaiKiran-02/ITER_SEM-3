'''
#
Q 01 If the input string is test = ‘Hello, How are you’, then
    a. Find the length of the above string
    b. Print only 2 characters from the last word of the string
    c. Find ‘hello’ in the above string
    d. Change the lowercase letter to uppercase of the above string and vice
       versa, Check if the string is in uppercase or not
    e. Separate the words of the string by a comma operator
    f. Replace the word ‘Hello’ by ‘Hi’
'''

test = "Hello, How are you"
# a.
print(len(test))
print(test.__len__())
print("----------")
# b.
print(test[-1:-3:-1])
print(test[-2:])
print("----------")
# c.
print(test[:5])
test_split = test.rsplit()
for i in test_split:
    if i == "Hello,":
        i = i.replace("Hello,","Hello")
        print(i)
        break
print("----------")
# d.
print(test.lower())
print(test.upper())
if test == test.upper():
    print(f"{True} , {test} has converted into upper case")
else:
    print(f"{False} , {test} has not changed.")
print("----------")
# e.
print(test.replace(" ", ","))
for i in test_split:
    i = i.replace(i,i+",")
    print(i, end ="")
print("----------")
# f.
print(test.replace("Hello","Hi"))
