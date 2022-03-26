#Write a program to display all prime numbers within a range

start=int(input("Enter a start number: "))
end=int(input("Enter a end number: "))
print("Prime numbers are: \n")
for n in range(start,end+1):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
        else:
                print(n)

