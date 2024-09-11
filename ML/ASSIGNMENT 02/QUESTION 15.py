gender = input("What is your Gender ( M or F ): ")[0]
first_name = input("First name: ")
last_name = input("Last name: ")
age = int(input("Age: "))

if ((gender.lower() == 'f')):
    if(age >= 20):
        married = input(f"Are you married {first_name} ? ( Y or N): ")
        if(married == 'y' or married == 'Y'):
            print(f"Then i shall call you Mrs. {first_name + last_name} ")
        else:
            print(f"Then i shall call you Ms. {first_name + last_name} ")
    else:
        print(f"Then i shall call you  {first_name + last_name} ")
else:
    if(age >= 20):
        print(f"Then i shall call you Mr. {first_name + last_name} ")
    else:
        print(f"Then i shall call you  {first_name + last_name} ")
               