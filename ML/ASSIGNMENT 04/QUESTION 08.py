'''
#
Q 08 Write a python program to separate an input word according to the vowels present in the
     string.
            For Example:
            test = ‘KlaGt’
            Result: [‘Kl’, ‘Gt’]
'''


word = input("Enter a word").split()[0]
l = []
for i in word:
    if i.lower() in ['a','e','i','o','u']:
        l = word.split(i)

print(l)