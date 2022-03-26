#Python program to print all Prime numbers in an Interval

start=int(input("Start number : "))
end=int(input("Enter end Number : "))
count=0
for i in range(start,end+1):
    if i>1:
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)
            count+=1
print("Number of prime number : ",count)