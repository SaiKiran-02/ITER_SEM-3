import calendar

month_num = int(input("Enter month: "))
year = int(input("Enter year: "))

month = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
} 

if(month_num in (1,3,5,7,8,10,12)):
    print(f"{month[month_num]} {year} had 31 days")
elif(month_num == 2):    
    if(calendar.isleap(year)):
        print(f"{month[month_num]} {year} had 29 days")
    else:
        print(f"{month[month_num]} {year} had 28 days")
else:
    print(f"{month[month_num]} {year} had 30 days")       

