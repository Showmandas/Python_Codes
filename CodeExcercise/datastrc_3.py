#Given a list slice it into 3 equal chunks and reverse each chunk
sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print('Original list ',sampleList)
chunk_1=sampleList[:3]
print('chunk_1: ',chunk_1)
revchunk_1=chunk_1[::-1]
print('After reversing it ',revchunk_1)
chunk_2=sampleList[3:6]
print('chunk_2: ',chunk_2)
revchunk_2=chunk_2[::-1]
print('After reversing it ',revchunk_2)
chunk_3=sampleList[6:9]
print('chunk_3: ',chunk_3)
revchunk_3=chunk_3[::-1]
print('After reversing it ',revchunk_3)
