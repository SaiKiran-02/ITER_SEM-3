'''
#
Q 11 Write a Python function that takes two file names, file1 and file2 as input. The function
     should read the contents of the file file1 line by line and should write them to another
     file file2 after adding a newline at the end of each line.
'''

def split_lines (file1 , file2):
    l = file1.readlines()
    for i in range( len(l) ):
        file2.writelines(l[i] + "\n")
    return file2.read()


file1 = open('python.txt','r')
file2 = open('splited_python.txt','w+')

print(split_lines(file1, file2))

file1.close()
file2.close()




