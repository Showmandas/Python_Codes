l=[3,4,5,2,3,7,6,4,1,5]
maxdupnum=max(set(l),key=l.count)
print(maxdupnum)
print("Original list :",l)
l=list(set(l))
print("After removing duplicates from the list: ",l)

