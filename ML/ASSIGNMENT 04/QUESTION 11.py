'''
#
Q 11 Write a program that requests a sentence, a word in the sentence, and another word and
     then displays the sentence with the first word replaced by the second.

     Example:
        Enter a sentence: What you don't know won't hurt you.
        Enter word to replace: know
        Enter replacement word: owe
        What you don't owe won't hurt you.
'''

sen = input("Enter a sentance: ")
word = input("Enter word to repplace: ").split()[0]
replace_word = input("Enter replacement word: ").split()[0]

newStr = sen.replace(word , replace_word)
print(newStr)