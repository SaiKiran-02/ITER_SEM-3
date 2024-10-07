'''
#
Q 10 Given two lists of numbers, each sorted in ascending order, merge them into a result list
     according to their order. Write function mergeList(values1, values2).

'''
from QUESTION_09 import remove_duplicate

def mergeList(l1 , l2):
     l1 = sorted(l1)
     l2 = sorted(l2)
     return sorted(l1+l2)

l1 = [6,23,4,1,2]
l2 = [1,2,9,5,6,6,3]
mergedList = mergeList(l1,l2)
print(remove_duplicate(mergedList))