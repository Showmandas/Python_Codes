# Given a list of numbers, Iterate it and print only those numbers which are divisible of 5

numberlist=[10,30,44,54,55]
print("Given list is :",numberlist)
print("Divisible by 5 in a list\n")

for i in range(0,len(numberlist)):
    if numberlist[i]%5==0:
         print(numberlist[i])