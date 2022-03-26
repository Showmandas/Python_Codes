#find average of N numbers

num = int(input("How many numbers do you enter? :"))
total_sum=0

for n in range(num):
    nums=float(input("Enter numbers :"))
    total_sum+=nums
avg=total_sum/num

print("Average Of Numbers : ",avg)
