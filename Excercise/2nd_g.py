
t=[]
h=int(input())
score=[]
for i in range(h):
    name=input()
    mark=float(input())
    t.append([name,mark])
    score.append(mark)

score=sorted(set(score))
m=score[1]
name=[]

for val in h:
    if m==val[1]:
        name.append(val[0])

for nm in name:
    print(nm)

# print(t)