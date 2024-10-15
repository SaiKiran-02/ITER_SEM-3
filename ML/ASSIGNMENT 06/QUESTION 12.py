'''
#
Q 12 Write a Python function that reads a file file1 and displays the number of words and the
     number of vowels in the file.
'''

def no_of_words(file):
    words = file.read().split()
    return len(words)


def no_of_vowels(file):
    vowels = 'aeiouAEIOU'
    c = 0
    num_vowels = sum(c+1 for char in file if char in vowels)
    return num_vowels

file = open('python.txt', 'r')
print(f"Number of vowels: {no_of_words(file)}")
print(f"Number of vowels: {no_of_vowels(file)}")
file.close()