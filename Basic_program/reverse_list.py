#Reversing a list

limit=int(input("Enter a limit : "))
listnum=[]

for i in range(limit):
    numlist=int(input())
    listnum.append(numlist)
print("Created list :",listnum)
print("Reverse list :",end=" ")
print(listnum[::-1])
