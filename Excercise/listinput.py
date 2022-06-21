#Accept a list of 5 float numbers as an input from the user

floatnum=[]
size=int(input("Enter size: "))

for i in range(0,size):
    print("Enter numbers according to size in their location: ",i)
    item=float(input())
    floatnum.append(item)

print(floatnum)