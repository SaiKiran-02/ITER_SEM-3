'''
#
Q 03 Write a function that takes two strings and returns True if they are anagrams and False
     otherwise. A pair of strings is anagrams if the letters in one word can be arranged to form
     the second one.
'''

def to_cheak_anagrams(str1 , str2):
    str1 = str1.lower()
    str2 = str2.lower()
    return sorted(str1) == sorted(str2)

str1 = "sai"
str2 = "ias"
if to_cheak_anagrams(str1,str2):
    print("anagram")
else:
    print("Not a anagaram")
