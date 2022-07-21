x = input()
m,n=[],[]
for i in x:
    if i.isalnum():
        m.append(i)
    else:
        n.append(i)
m.sort()
k,l=0,0
for i in x:
    if i.isalnum():
        print(m[k],end="")
        k+=1
    else:
        print(n[l],end="")
        l+=1