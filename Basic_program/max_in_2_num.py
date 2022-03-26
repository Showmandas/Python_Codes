# Maximum of two numbers in Python

num1=2
num2=3

# print(max(num1,num2))

# using function

#def max_num(a,b):
#     if a>b:
#         print("a is greater than b and it's :",end=" ")
#         print(a)
#     else:
#         print("b is greater than a and it's : ", end=" ")
#         print(b)
#
# max_num(4,3)
#
# numlist=[2,3,5,6]
# print(max(numlist))

def max_num(*a):
    maxnum=[*a]
    print(max(maxnum))

max_num(2,5,46,6,70)