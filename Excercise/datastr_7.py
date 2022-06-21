#Given two sets, Checks if One Set is a subset or superset of another Set. if the subset is found delete all elements from that set
firstSet = {27, 43, 34}
secondSet = {34, 93, 22, 27, 43, 53, 48}
print("First set: ",firstSet)
print("Second set: ",secondSet)
print("First set is subset of second set -",firstSet.issubset(secondSet))
print("Second set is subset of first set -",secondSet.issubset(firstSet))
print("First set is Super set of second set -",firstSet.issuperset(secondSet))
print("Second set is Super set of first set -",secondSet.issuperset(firstSet))
if(firstSet.issubset(secondSet)):
    firstSet.clear()
if(secondSet.issubset(firstSet)):
    secondSet.clear()

print("First Set :",firstSet)
print("Second Set :",secondSet)