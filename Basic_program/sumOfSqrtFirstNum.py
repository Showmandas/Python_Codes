#Python Program for Sum of squares of first n natural numbers





#just print the list of  square numbers
# for i in range(0,n):
#     num=int(input())
#     lst.append(num*num)
#     s=s+num
# print(s)
def Sum_sqr_num(n):
    s=0
    for i in range(1,n+1):
        s=s+(i*i)
    return s
n=int(input("Enter limit: "))
sqrnum=Sum_sqr_num(n)
print(sqrnum)

