'''
#
Q 09 Write a Python program to get a string made of the first 2 and last 2 characters of a given
     string. If the string length is less than 2, return the empty string instead.

     Examples:
         Sample String: 'w3resource'
         Expected Result: 'w3ce'
         Sample String: 'w3'
         Expected Result: 'w3w3'
         Sample String: 'w'
         Expected Result: Empty String
'''

def newString(str):
    nStr = ""
    if len(str) < 2:
        return "Empty String"
    else:
        nStr = str[:2] + str[len(str)-2:]
    return nStr

str = input("Enter a string:")
print(newString(str))


