#Remove duplicate from a list and create a tuple and find the minimum and maximum number
sampleList = [87, 45, 41, 65, 94, 41, 99, 94]

sampleList=list(dict.fromkeys(sampleList))
print("unique items :",sampleList)
print("Max",max(sampleList))
print("Min",min(sampleList))