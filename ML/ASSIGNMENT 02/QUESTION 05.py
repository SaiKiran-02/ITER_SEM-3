print("write a , b and c of quadratic equation which follows this equation: ax^2 + bx + c = 0")
a = float(input("Enter a? "))
b = float(input("Enter b? "))
c = float(input("Enter c? "))

d = (b**2) - (4*a*c)
root1 = (-b + d ** 0.5) / 2 * a
root2 = (-b - d ** 0.5) / 2 * a
if (d > 0):
    print(f"Discriminant is posite so the equation has two real roots: {root1} and {root2}")
elif (d == 0):
    print(f"The equation has positive discriminant so it contains only one real root: {root1}")
else:
    print("the equation has no real roots.")



