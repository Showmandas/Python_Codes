# Given a list of numbers, return True if first and last number of a list is same

# listnum=[39,30,40,20,40,59]
# print("Given list is: ",listnum)
#
# firstelem=listnum[0]
# lastelem=listnum[-1]
#
# if (firstelem == lastelem):
#     return True
# else:
#     return False

def listnum(list):
    print("Given List :",list)
    firstelem=list[0]
    lastelem=list[-1]
    if (firstelem  == lastelem):
         return True
    else:
        return False

numlist=[10,20,30,20,10]
print(listnum(numlist))
