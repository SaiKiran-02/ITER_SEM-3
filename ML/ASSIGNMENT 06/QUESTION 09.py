'''
#
Q 09 A palindrome is a word that reads the same from the front and the back. You can extend
     this definition to the digits of a number. Write recursive function
     is_number_palindrome(number) but without converting the number into a string and
     then using string functionalities like [::-1].
'''

def is_number_palindrome(number):
    # Helper function to find the reverse of the number recursively
    def is_palindrome_recursive(n, reverse=0):
        if n == 0:
            return reverse
        else:
            reverse = reverse * 10 + n % 10
            return is_palindrome_recursive(n // 10, reverse)
    if number < 0:
        return False
    reversed_number = is_palindrome_recursive(number)

    return number == reversed_number

n = int(input("Enter a number: "))
print(is_number_palindrome(n))