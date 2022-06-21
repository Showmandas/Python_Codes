# def sum(*a):
#     result=0
#     for i in a:
#         result=result+i
#     return result
#
# res=sum(2,3,4,5)
# print(res)

def square(*a):
    l=list(a)
    sl=[a**2 for a in l]
    return sl

res=square(2,3)
print(res)