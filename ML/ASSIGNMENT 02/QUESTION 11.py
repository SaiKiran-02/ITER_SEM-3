weight = float(input("Enetr your weight in kg: "))
height = float(input("Enetr your height in meter: "))

bmi = weight / height**2

if(bmi < 18.5):
    print("Under Weight")
elif(bmi < 24.9):
    print("normal weight")
elif(bmi < 29.9):
    print("over weight")
else:
    print("obese")            