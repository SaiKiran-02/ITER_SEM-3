import math

print("""

    .-'''-.                                             
   '   _    \      _               _ ..-'''-.   _       
 /   /` '.   \   .' )   _..._     /_\\.-'''\ \ ( `.     
.   |     \  '  / .'  .'     '.  // \\      | | '. \    
|   '      |  '/ /   .   .-.   .|/   \|  __/ /    \ \   
\    \     / // /    |  '   '  |        |_  '.     \ \  
 `.   ` ..' /. '     |  |   |  |           `.  \    ' . 
    '-...-'` | |     |  |   |  |             \ '.   | | 
             ' '     |  |   |  |              , |   ' ' 
              \ \    |  |   |  |              | |  / /  
               \ \   |  |   |  |             / ,' / /   
                \ '. |  |   |  |     -....--'  /.' /    
                 '._)'--'   '--'     `.. __..-'(_.'     

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

    .-'''-.                                                
   '   _    \      _               _       .-''-.  _       
 /   /` '.   \   .' )   _..._     /_\    .' .-.  )( `.     
.   |     \  '  / .'  .'     '.  // \\  / .'  / /  '. \    
|   '      |  '/ /   .   .-.   .|/   \|(_/   / /     \ \   
\    \     / // /    |  '   '  |            / /       \ \  
 `.   ` ..' /. '     |  |   |  |           / /         ' . 
    '-...-'` | |     |  |   |  |          . '          | | 
             ' '     |  |   |  |         / /    _.-')  ' ' 
              \ \    |  |   |  |       .' '  _.'.-''  / /  
               \ \   |  |   |  |      /  /.-'_.'     / /   
                \ '. |  |   |  |     /    _.'      .' /    
                 '._)'--'   '--'    ( _.-'        (_.'     


""")

count1 = 0
for i in range(1,101):
    for j in range(1,101):
        k_squared = i**2 + j**2
        k = int(math.sqrt(k_squared))

        if k_squared == k**2 and k<101:
            print(f"{i}^2 + {j}^2 = {k}^2   :   {i ** 2} + {j ** 2} = {k ** 2}")
            count1 += 1

print(count1)