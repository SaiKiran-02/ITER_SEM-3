'''
#
Q 04 Write a python program to replace that character, which is repeated maximum time in
     each string by ‘-’ (dash).
'''

def max_repeated_replace(str):

    dict = {}
    for i in str:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    max_char = max(dict, key=(dict.get))
    modified_string = str.replace(max_char, '-')

    return modified_string


str = input("enter string: ")
print (max_repeated_replace(str))


