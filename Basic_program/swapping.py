#Python program to swap two elements in a list

def swapping(swplist):
    swplist[0],swplist[2]=swplist[2],swplist[0]
    return swplist

swplist=[2,3,4,1]
print(swapping(swplist))