#Given two lists create a third list by picking an odd-index element from the first list and even index elements from the second.
listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]

oddIndex=listOne[1::2]
evenIndex=listTwo[::2]
print("Element at odd-index positions from list one")
print(oddIndex)
print("Element at even-index positions from list two")
print(evenIndex)
print("Printing Final third list")
print(oddIndex+evenIndex)

