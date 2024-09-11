n = int(input("Enter an Integer: "))

print(f"Is {n} divisible by 5 and 6? ", (n % 5 == 0 and n % 6 == 0))
print(f"Is {n} divisible by 5 or 6? ", (n % 5 == 0 or n % 6 == 0))
print(f"Is {n} divisible by 5 or 6 , But not by both. ", ((n % 5 == 0 or n % 6 == 0)  or (n % 5 == 0 and n % 6 == 0) ) )
        