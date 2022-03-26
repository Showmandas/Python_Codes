# Python Program for factorial of a number
# import math
# def factorial(n):
#     return math.factorial(n)
#
# factnum=factorial(5)
# print(factnum)

n=int(input("Enter a number :"))
def factorial(n):
    return 1 if(n==1 or n==0) else n*factorial(n-1)

factnum=factorial(n)
print(factnum)
