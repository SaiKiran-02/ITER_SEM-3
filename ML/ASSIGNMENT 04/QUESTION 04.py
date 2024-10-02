'''
#
Q 04 Write a python program to replace that character, which is repeated maximum time in
     each string by ‘-’ (dash).
'''


def max_repeated_replace(str):
    c = 0
    s = []
    for i in range(len(str)):
        print(str[i] , end = " : ")
        for j in range(i,len(str)):
           if str[i] != str[j]:
               c = c+1
           else:
               continue
        print(c)
        s.append(((str[i], c)))
        c = 0
    print(s)



str = input("enter string: ")
print (max_repeated_replace(str))


