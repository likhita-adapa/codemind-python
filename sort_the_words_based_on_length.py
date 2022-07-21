x=list(map(str,input().split()))
l=[]
for i in x:
    c=0
    for j in i:
        c+=ord(j)
    l.append([c,i])
l.sort()
for a in l:
    print(a[1],end=" ")