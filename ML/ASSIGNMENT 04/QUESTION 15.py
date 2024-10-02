'''
#
Q 15 Pig Latin takes the first consonant of a word, moves it to the end of the word and adds
     on an “ay”. If a word begins with a vowel you just add “way” to the end. For example,
     pig becomes igpay, banana becomes ananabay, and aadvark becomes aadvarkway.
     Create a program that will ask the user to enter a word and change it into Pig Latin.
     Make sure the new word is displayed in lower case.
'''

word = input("Enter word: ")
if word[0].upper() in ('A','E','I','O','U'):
    word = word + "way"
else:
    word = word[1:] + word[0].lower() + "ay"
print (word)
