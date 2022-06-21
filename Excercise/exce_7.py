# Given a list, iterate it, and display numbers divisible by five, and if you find a number greater than 150, stop the loop iteration.

list1=[12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for i in range(0,len(list1)):
    if list1[i]%5==0:
        print(list1[i])
    if list1[i] >= 150:
        break
