#Check if element exists in list in Python

inpnum=int(input("Enter limit for creating a list :"))
listnum=[]

for l in range(inpnum):
    nums=int(input())
    listnum.append(nums)
print("Created List :",end=' ')
print(listnum)

givnum=int(input("Enter number to check existence of element in the list : "))
test_list=set(listnum)
if givnum in test_list:
    print("Exist")
else:
    print("Not exist")

print("After checking autiomatice clear the list: ")
listnum.clear()
print(listnum)
