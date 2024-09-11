print("Tow linear eqaution is in the form of : ( ax + by = e )  and ( cx + dy = f )/nWrite the values of a ,b ,c ,d ,e ,f .")
a = float(input("Enter a? "))
b = float(input("Enter b? "))
c = float(input("Enter c? "))
d = float(input("Enter d? "))
e = float(input("Enter e? "))
f = float(input("Enter f? "))

denominator = a*d - b*c

if(denominator == 0):
    print("The equation has no solution")
else:
    x = (e*d - b*f) / denominator
    y = (a * f - e * c) / denominator
    print(f"x is {x} and y is {y}")