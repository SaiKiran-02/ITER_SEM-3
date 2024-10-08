'''
#
Q 05 Write recursive function reverse_string(text) that flips the letters of the text passed
in.
'''

def reverse_string(test,rev_text = []):
    if len(test) == 1:
        rev_text.append(test[0])
        return "".join(rev_text)
    else:
        rev_text.append(test[-1])
        return reverse_string(test[:len(test)-1])

print(reverse_string("Sai kiran"))
