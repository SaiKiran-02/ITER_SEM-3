n = int(input("Enter 4 digit number: "))
sum =0
temp =n
while(temp!=0):
    rem = temp%10
    sum = sum+rem
    temp = temp//10

print(f"sum of the digits of {n} is {sum} ")