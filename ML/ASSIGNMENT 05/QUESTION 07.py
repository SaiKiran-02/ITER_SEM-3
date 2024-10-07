'''
#
Q 07 Define a function to multiply two matrices.

     For example, for two 3 * 3 matrices a and b, c is
     where c௜௝ = a௜ଵ ∗ bଵ௝ + a௜ଶ ∗ bଶ௝ + a௜ଷ ∗ bଷ௝. Write a Python program that prompts the user to enter two 3 * 3 matrices and displays
     their product.
'''
from QUESTION_06 import createMat , showMat
def multiplyMat(a , b):
    c = [[0 for _ in range(3)] for _ in range(3)]
    if len(a[1]) == len(b):
        for i in range(len(a)):
            for j in range(len(b[1])):
                for k in range(len(b[1])):
                    c[i][j] += a[i][k] *b [k][i]
    else:
        print("Matrix multiplication not possible.")

    return c


print("Enter matrix 01: ")
mat1 = createMat(3,3)
print("Enter matrix 02: ")
mat2 = createMat(3,3)

print("Matrix 01: ")
showMat(mat1)
print("Matrix 02: ")
showMat(mat2)

resultedMat = multiplyMat(mat1, mat2)
print("Resulted matrix: ")
showMat(resultedMat)                                       # transpose required.



