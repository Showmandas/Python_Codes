#Given a string, display only those characters which are present at an even index number.

str = "pynative"

print("Original string is :", str)
print("Printing only even index chars : ")
for i in range(0, len(str)-1, 2):
    print(str[i])