'''
#
Q 10 Write a Python program to get a string from a given string where all occurrences of its
     first char have been changed to '$', except the first char itself.

     Examples:
         Sample String: 'restart'
         Expected Result: 'resta$t'
'''

def setLetters(str):

    newStr =str[0]
    for i in str[1:].lower():
        if i == str[0].lower():
            newStr += "$"
        else:
            newStr += i
    return newStr


str = input("Enter a string:")
print(setLetters(str))