import random as r

while 1:
    print("Enter what you wnat.")
    user = int(input("scissor: (0) , rock (1) , paper (2): " ))
    computer = r.randint(0,3)

    if(computer == user ):
        print("it is a Draw")
    else:
        if((user == 0 and computer == 1) or (user == 1 and computer == 2) or (user == 2 and computer == 0)):
            print(f"computer throughs {computer}. bad luck! better luck next time.")
        else:
              print(f"computer throughs {computer}. WOW! Congratulations YOU WON.")  
