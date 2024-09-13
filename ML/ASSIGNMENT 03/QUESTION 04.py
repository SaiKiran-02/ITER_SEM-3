def calc_armstromg_numbers():
    for x in range(1, 11):
        for y in range(1, 11):
            for z in range(1, 11):
                if (x*100 + y*10 + z == x**3 + y**3 + z**3):
                    print(f"{x}*100 + {y}*10 + {z} == {x**3} + {y**3}+ {z**3}    ::   {x**3} + {y**3}+ {z**3} = {x**3 + y**3 + z**3}")
                    x_list.append(x)
                    y_list.append(y)
                    z_list.append(z)

x_list = []
y_list = []
z_list = []

calc_armstromg_numbers()

print("x        y         z")
print("---------------------")
for i in range(0,list.__len__(x_list)) :
    print(f"""{x_list[i]}        {y_list[i]}         {z_list[i]}""")

