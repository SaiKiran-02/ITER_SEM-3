
def to_binary(n):
    if n == 0:
        return "0"

    binary = ""
    while n > 0:
        rem = n % 2
        binary = str(rem) + binary
        n = n // 2

    return binary


n = int(input("Enter the number you want to convert into binary: "))
print(to_binary(n))
