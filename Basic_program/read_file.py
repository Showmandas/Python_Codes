#Reading a file

file=open("lines.txt",'r+')
# print(file.readable())
# txt=file.read()
# print(txt)
# len=len(txt)
# print(len)
for line in file:
    print(line)
file.close()