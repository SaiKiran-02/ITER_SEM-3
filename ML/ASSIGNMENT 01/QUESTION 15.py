num_days = int(input("Enter the Number of day: "))
num_hours = int(input("Enter the Number of hours: "))
num_min = int(input("Enter the Number of min: "))
num_sec = int(input("Enter the Number of sec: "))

total_sec = (num_days * 3600 * 24) + (num_hours * 3600 ) + (num_min * 60) + num_sec

print(f"total sec : {total_sec}")