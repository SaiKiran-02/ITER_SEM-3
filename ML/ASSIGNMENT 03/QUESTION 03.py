print("""
 ___          ___   ___
|   |   /   |/   \\  .'.  \\
|   |  |    |     |  --'  | 
 ---    \\   |     |      /
""")

print("a^2 + b^2 = c^2")
print("----------------")
count = 0
for i in range(1,101):
    for j in range(1,101):
        for k in range(1,101):
            if( i**2 + j**2 == k**2):
                print(f"{i}^2 + {j}^2 = {k}^2   :   {i**2} + {j**2} = {k**2}")
                count+=1
print(count)


print("""
 ___          ___   ___
|   |   /   |/   \\  .:  \\
|   |  |    |     |  '--  | 
 ---    \\   |     |      /
""")

count1 = 0
k = 1
for i in range(1,101):
    for j in range(1,101):
        if( i**2 + j**2 == k**2):
            print(f"{i}^2 + {j}^2 = {k}^2   :   {i**2} + {j**2} = {k**2}")
            count1 += 1
            k += 1
        else:
            k+=1



print(count1)