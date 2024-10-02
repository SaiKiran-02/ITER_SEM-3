'''
#
Q 13 Ask the user to type in a word in upper case. If they type it in lower case, ask them to
     try again. Keep repeating this until they type in a message all in uppercase.
'''

word = input("Enter Upper case word: ").split()[0]

while word.isupper()==False:
    print("Try again.")
    word = input("Enter Upper case word: ").split()[0]

print(word + " is in upper case")