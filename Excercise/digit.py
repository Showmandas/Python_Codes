#Given a number count the total number of digits in a number

digit=input("Enter a digit: ")
numOfDigits=0
for x in digit:
  if x >= '0' and x <= '9':
     numOfDigits=numOfDigits+1
print(numOfDigits)
