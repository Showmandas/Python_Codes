n=[]
size=int(input("Number: "))
score=[]
for i in range(size):
    name=input()
    marks=float(input())
    n.append([name,marks])
    score.append(marks)
    # score.sort()
score=sorted(set(score))
m=score[1]
# print(m)
name=[]
for val in n:
    if m==val[1]:
        name.append(val[0])

name.sort()
for nm in name:
    print(nm)

