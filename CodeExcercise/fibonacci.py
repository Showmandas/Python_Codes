#Display Fibonacci series up to 10 terms

terms=10
n1,n2=0,1
count=0
print("Fibonacci sereis: \n")

while count < terms:
    print(n1,end=' ')
    temp=n1+n2
    n1=n2
    n2=temp
    count+=1
print(temp)
