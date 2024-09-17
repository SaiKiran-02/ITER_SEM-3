def to_octal(n):
    if n == 0:
        return "0"

    octal = ""
    while n > 0:
        rem = n % 8
        octal = str(rem) + octal  # Corrected: append to `octal` instead of `binary`
        n = n // 8

    return octal

def to_hex(n):
    if n == 0:
        return "0"

    hex_digits = "0123456789ABCDEF"
    hex_value = ""
    while n > 0:
        rem = n % 16
        hex_value = hex_digits[rem] + hex_value
        n = n // 16

    return hex_value


print("Octal representation of 8:", to_octal(8))
print("Hexadecimal representation of 255:", to_hex(255))
