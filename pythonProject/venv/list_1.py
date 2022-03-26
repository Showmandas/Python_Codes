#List

subjects=["javascript","java","os","toc","c++","coa"]
print(subjects)

#print first index
print(subjects[0])

#print elements after 2 index
print(subjects[2:])

#add elements
print(subjects + ["python","3"])

#determine length of list
print("Length of list is :",len(subjects))

#append element
subjects.append('compiler')
print(subjects)

#insert
subjects.insert(2,'go')
print(subjects)

#remove
subjects.remove("go")
print(subjects)

#sort and reverse
subjects.sort()
print(subjects)
subjects.reverse()
print(subjects)

#range
num=list(range(10))
print(num)
num1=list(range(5,10))
print(num1)

num2=list(range(2,100,3))
print(num2)
