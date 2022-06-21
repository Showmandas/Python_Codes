#Given a list, remove the element at index 4 and add it to the 2nd position and at the end of the list
list1=[34, 54, 67, 89, 11, 43, 94]
print("original list ",list1)
remvind=list1.pop(4)
print('List After removing element at index 4  ',list1)
addind=list1.insert(2,remvind);
print('List after Adding element at index 2  ',list1)
lastind=list1.append(11)
print(list1)