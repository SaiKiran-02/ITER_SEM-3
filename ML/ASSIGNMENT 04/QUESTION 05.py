'''
#
Q 05 Write a function that takes a sentence as an input parameter and displays the number of
     words in the sentence.
'''
def count_num_of_words(sen):
    words = sen.split()
    return len(words)


sen = input("Enter a sentance: ")
print(count_num_of_words(sen))