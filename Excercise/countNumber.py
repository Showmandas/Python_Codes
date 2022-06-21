# Count the total number of digits in a number

n=int(input("Enter number :"))
#without loop
# digit=str(n)
# print(len(digit))

count=0
while n!=0:
    n=n//10
    count=count+1
print(count)