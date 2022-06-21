# Iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element
import collections

list1=[11, 45, 8, 11, 23, 45, 23, 45, 89]
print('Original List: ',list1)
countitem=collections.Counter(list1)
print('Printing count of each item   ',countitem)