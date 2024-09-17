def sum_of_proper_divisors(n):
    divisors_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i

    return divisors_sum

def calc_friends(a, b):
    if a == b:
        return False

    sum_a = sum_of_proper_divisors(a)
    sum_b = sum_of_proper_divisors(b)

    return sum_a == b and sum_b == a

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if calc_friends(num1, num2):
    print(f"{num1} and {num2} are friendly numbers.")
else:
    print(f"{num1} and {num2} are not friendly numbers.")
