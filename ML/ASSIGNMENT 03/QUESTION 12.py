#(a)
for i in range(6):
    print('* '*i)
print("===============================")
# (b)
for i in range(6):
    for j in range(1,i+1):
        print(j, end=" ")
    print("")

print("===============================")

# (c)
for i in range(6):
    for j in range(1,i+1):
        print(i, end=" ")
    print("")

print("-------------------------------")

for i in range(1,6):
    print(str(i)*i)

# (d)
c = 1
for i in range(6):
    for j in range(1,i+1):
        print(c, end=" ")
        c+=1
    print("")
print("===============================")