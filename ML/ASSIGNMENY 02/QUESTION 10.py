dic = {
    0 : "Sunday",
    1 : "Monday",
    2 : "Tuesday",
    3 : "Wednesday",
    4 : "Thrusday",
    5 : "Friday",
    6 : "Saturday"
}

for i in dic:
    print(i, "-->",dic[i])

today = int(input("Enter today's day: "))
num_of_days = int(input("Enter the number of days elapsed since today: "))
future_day = 0

if(num_of_days < 7):
    future_day = (today + num_of_days) % 7
else:
    rem =  num_of_days % 7
    future_day = today + rem


if(future_day == 0):
    print(f"Today is {dic[today]} and Future day is {dic[future_day]}")
elif(future_day == 1):
    print(f"Today is {dic[today]} and Future day is {dic[future_day]}")
elif(future_day == 2):
    print(f"Today is {dic[today]} and Future day is {dic[future_day]}")
elif(future_day == 3):
    print(f"Today is {dic[today]} and Future day is {dic[future_day]}")
elif(future_day == 4):
    print(f"Today is {dic[today]} and Future day is {dic[future_day]}")
elif(future_day == 5):
    print(f"Today is {dic[today]} and Future day is {dic[future_day]}")
elif(future_day == 6):
    print(f"Today is {dic[today]} and Future day is {dic[future_day]}")