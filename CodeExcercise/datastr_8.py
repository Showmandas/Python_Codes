#Iterate a given list and Check if a given element already exists in a dictionary as a key’s value if not delete it from the list
rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict ={'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

def myfun(x):
    if rollNumber in sampleDict:
        return True
    else:
        return False

remele=filter(myfun,sampleDict)
for x in remele.values():
    print(x)