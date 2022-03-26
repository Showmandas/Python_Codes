#Python program to interchange first and last elements in a list
def reverselist(newlist):
    newlist[0],newlist[-1]=newlist[-1],newlist[0]
    return newlist

newlist=[1,2,3,4,5]
print(reverselist(newlist))