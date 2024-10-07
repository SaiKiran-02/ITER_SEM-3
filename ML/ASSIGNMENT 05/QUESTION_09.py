'''
#
Q 09 You are supposed to remove duplicate entries from a list. The constraint is that the
     original order should be preserved. Write function remove_duplicates(values).
'''

def remove_duplicate(l):
    new_l = []
    for i in l:
        if i not in new_l :
            new_l.append(i)
    return new_l

def main():
    print("Enter 10 Integer values: ")
    l = []
    for i in range(10):
        try:
            item = int(input("Enetr number: "))
            l.append(item)
        except ValueError:
            print(ValueError)
            print("Enter Integer values only. ")
    new_l = remove_duplicate(l)
    print(new_l)

if __name__ == "__main__":
    main()
