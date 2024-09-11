print("Enter the X and Y co-ordinates: ")
x = float(input("X = "))
y = float(input("Y = "))

if(x > 0 and y > 0):
    print(f"point lies on I quadrant.\nPoint is : ({x},{y})")
elif(x < 0 and y > 0):
    print(f"Point lies on II quadrant.\nPoint is : ({x},{y})")
elif(x < 0 and y < 0):
    print(f"Point lies on III quadrant.\nPoint is : ({x},{y})")
elif(x > 0 and y < 0):
    print(f"Point lies on IV quadrant.\nPoint is : ({x},{y})")
elif(x == 0 and y!= 0):
    print(f"Point lies on Y axis.\nPoint is : ({x},{y})")
elif(y == 0 and x != 0):
    print(f"Point lies on X axis.\nPoint is : ({x},{y})")
else:
    print(f"point is in origin.\npoint is : ({x},{y})")



