print("Enter the age of Rahul and Ayush.")
age_rahul = int(input("Rahul's age = "))
age_ayush = int(input("Ayush's age = "))

if(age_ayush > age_rahul):
    print(f"Rahul is elder.")
elif(age_ayush < age_rahul):
    print("Ayush is elder.")
else:
    print("Rahul and Ayush have same age.")
