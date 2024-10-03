'''
#
Q 08 Write a python program to separate an input word according to the vowels present in the
     string.
            For Example:
            test = ‘KlaGt’
            Result: [‘Kl’, ‘Gt’]
'''


def separate_by_vowels(word):
    vowels = 'aeiouAEIOU'
    result = []
    temp = ''

    for char in word:
        if char in vowels:
            if temp:
                result.append(temp)
                temp = ''
        else:
            temp += char

    if temp:
        result.append(temp)

    return result


# Example usage
test = 'KlaGt'
print(separate_by_vowels(test))  # Output: ['Kl', 'Gt']