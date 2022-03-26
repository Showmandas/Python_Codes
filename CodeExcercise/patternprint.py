#Print the following pattern using for loop

n=int(input("Enter number of rows: "))

for i in range(0,n+1):
    for c in range(n-i,0,-1):
        print(c,end=' ')
    print('')
