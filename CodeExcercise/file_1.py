#file IO

file1=open('das.txt','wb')
print(file1.mode)
print(file1.name)
file1.write(bytes("Write something in this file",'utf-8'))
file1.close()