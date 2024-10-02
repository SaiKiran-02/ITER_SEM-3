'''
#
Q 14 Ask the user to type in a word and then display it backwards on separate lines. For
     instance, if they type in “Hello” it should display as shown below:
     
     Example:
     Enter a word: Hello
o
l
l
e
H
'''

word = input("Enter word: ")
for i in range(len(word)-1,-1,-1):
    print(word[i])
print("----------------------------------")
word = word[::-1]
for i in word:
    print(i)