#Python Program to find sum of array

arr=int(input("Enter limit : "))
numarr=[]
sum=0
mul=1
for inp in range(1,arr+1):
    num=int(input())
    numarr.append(num)
    sum=sum+num
    mul=mul*num
print("List of numbers : ",numarr)
print("Sum of these numbers :",sum)
print("Multiply of these numbers :",mul)
print("Maximum of these numbers :",max(numarr))
print("Minimum of these numbers :",min(numarr))