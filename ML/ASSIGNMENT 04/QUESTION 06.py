'''
#
Q 06 Write a function that takes a sentence as an input parameter and replaces the first letter
     of every word with the corresponding uppercase letter and rest of the letters in the word
     by corresponding letters in lowercase without using built-in function.
'''

def capitalise_first_letter_of_words(sen):
    words = sen.split()
    newWords =[]
    for i in words:
        nl = i[0].upper()
        for j in range(1,len(i)):
            nl += i[j]
            # if j == len(i)-1:
            #     nl+=" "
        nl+= " "
        newWords.append(nl)
    return "".join(newWords)




sen = input("Enter a sentance: ")
print(capitalise_first_letter_of_words(sen))