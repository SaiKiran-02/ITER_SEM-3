def is_number_pallindrome(num):
    temp = num
    n = 0
    while(temp != 0):
        rem = temp % 10
        n = (n * 10 )+ rem
        temp = temp // 10

    if(n == num):
        print("pallindrome")
    else:
        print("not pallindrome")


n = int(input("Enter the number:"))
is_number_pallindrome(n)