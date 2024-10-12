'''
#
Q 11 Write a Python function that takes two file names, file1 and file2 as input. The function
     should read the contents of the file file1 line by line and should write them to another
     file file2 after adding a newline at the end of each line.
'''

def split_lines (file1 , file2):
    [ file2.writelines(i + "\n") for i in file1.readlines() ]
    print("file is splited.")
    return file2

file1 = open('python.txt','r')
file2 = open('splited_python.txt','w')

print(split_lines(file1, file2))




