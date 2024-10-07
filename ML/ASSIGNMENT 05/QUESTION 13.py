'''
#
Q 13 Add to program in Q 12 to ask the user to enter a number and display the country in
     that position.
'''

import QUESTION_12

index = int(input("Enter a number: "))
try:
    print(f"{index} ---> {QUESTION_12.countries[index]}")
except Exception :
    print("Index is out of bound.")
