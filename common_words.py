x=list(map(str,input().lower().split()))
y=list(map(str,input().lower().split()))
l,m=[],[]
for i in x:
    if i in y:
        l.append(i)
for i in y:
    if i in x:
        m.append(i)
for i in m:
    if i in l:
        print(i,end=" ")