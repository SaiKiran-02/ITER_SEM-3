def calc_friends(max_exclusive):
    sum_i, sum_j = 0 , 0
    for i in range(1,max_exclusive+1):
        for j in range(1,i+1):
            if (i % j == 0):
                sum_i += j
            for k in range(1,j+1):
                if(j % k == 0):
                    sum_j += k
            if (sum_j == i and sum_i == j):
                print(f"sum_j = {sum_j} and i = {i} , sum_i = {sum_i} and j = {j}")

n = int(input("Enter the number:"))
calc_friends(n)