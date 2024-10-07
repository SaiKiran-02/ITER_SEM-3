'''
#
Q 15 Write a program that prints a histogram of frequencies of characters occurring in a
     message supplied by the user.
'''
import matplotlib.pyplot as plt
msg = input("Emter your message: ")
d = {}
for i in msg.lower():
    d.update({i:msg.count(i)})
print(d)
plt.ylabel = "frequency of charecters"
plt.xlabel = "charecters"
plt.bar(d.keys(),d.values() ,color= "green")
plt.show()

