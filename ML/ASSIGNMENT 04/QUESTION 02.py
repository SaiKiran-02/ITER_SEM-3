'''
#
Q 02 Write a function that takes a string as a parameter and returns a string with every
successive repetitive character replaced with a star(*).
    For example,
    'balloon'
    is returned as
    'bal*o*n'
'''

def replace_successive_repeater(str):
    str_new = []
    for i in range(len(str)):
        if str[i] == str[i-1]:
            str_new.append("*")
        else:
            str_new.append(str[i])
    str_new = "".join(str_new)
    return str_new

str = input("Enter a string: ")
print(replace_successive_repeater(str))
