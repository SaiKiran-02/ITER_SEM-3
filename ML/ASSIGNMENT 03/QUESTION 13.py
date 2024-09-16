c = 0
for i in range(100,1001):
    if ( i%5==0 and i%6==0 ):
        c+=1
        print(i,end=" ")
    if c == 10:
        print("")
        c=0