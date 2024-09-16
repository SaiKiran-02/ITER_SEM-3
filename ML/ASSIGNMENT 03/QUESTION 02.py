
sum = 0
def calc_checksum(digits):
    global sum
    for i in digits:
        sum = sum + int(i)*(digits.index(i)+1)
    return sum%10



digits = input("Enter a number: ")
print(calc_checksum(digits))
