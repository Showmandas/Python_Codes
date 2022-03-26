# Print the following pattern
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

row=int(input("enter row: "))
for r in range(row+1):
    for c in range(r):
        print(c+1,end=' ')
    print(" ")