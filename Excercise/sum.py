#Accept number from user and calculate the sum of all number from 1 to a given number

num=input("Enter numbers: ")

list=num.split()

sum=0

for n in list:
    sum=sum+int(n)
print("Sum of given numbers: ",sum)