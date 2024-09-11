ch = input("Enter a charecter: ")[0]

if ((ch >= 65) & (ch <= 90)):
    print("Capital case")
elif ((ch >= 97) & (ch <= 122)):
    print("Lower case")
elif ((ch>= 48) & (ch<= 57)):
    print("numbers")
else:
    print("Special Symbols")