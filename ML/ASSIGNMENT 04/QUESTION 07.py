'''
#
Q 07 Write a python program to count the number of odd and even length words present in a
     string.
'''

str = "Number of even words in 'i am a coder and i know how to hack your life."

l = str.split()
c_even , c_odd = 0 , 0
for i in l:
    if len(i)%2 == 0:
        c_even += 1
    else:
        c_odd += 1
print (f"Number of even words in '{str}' is {c_even} \nNumber of odd words in '{str}' is {c_odd}")
