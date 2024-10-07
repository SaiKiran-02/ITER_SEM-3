'''
#
Q 06 Define a function to add two matrices. In order to be added, the two matrices must have
     the same dimensions and the same or compatible types of elements. Let c be the resulting
     matrix. Each element c௜௝ is a௜௝ + b௜௝. For example, for two 3 * 3 matrices a and b, c is

     Write a Python program that prompts the user to enter two 3 * 3 matrices and displays
     their sum.
'''

def addMatrix(a,b):
    c = []
    if len(a) == len(b) and len(a[1]) == len(b[1]):
        for i in range(len(a)):
            c_item = []
            for j in range(len(a[i])):
                     c_item.append(a[i][j]+b[i][j])
            c.append(c_item)
    return c


def createMat(n,m):
    l = []
    for i in range(n):
        tem_l = []
        for j in range(m):
            item = float(input(f"Enter {i} row element: "))
            tem_l.append(item)
        l.append(tem_l)
    return l
def showMat(mat):
    [print(i) for i in mat]

if __name__ == '__main__':
    print("Enter matrix 01: ")
    mat1 = createMat(4,4)
    print("Enter matrix 02: ")
    mat2 = createMat(4,4)

    print("matrix 01:")
    showMat(mat1)
    print("matrix 02:")
    showMat(mat2)

    print("resulted matrix:")
    resultedMat = addMatrix(mat1,mat2)
    showMat(resultedMat)