s=list(map(str,input().split()))
b=[]
c=[]
for i in s:
    for j in i:
        if j=='a':
            b.append(j)
        elif j=='e':
            b.append(j)
        elif j=='i':
            b.append(j)
        elif j=='o':
            b.append(j)
        elif j=='u':
            b.append(j)
        elif j=='A':
            c.append(j)
        elif j=='E':
            c.append(j)
        elif j=='I':
            c.append(j)
        elif j=='O':
            c.append(j)
        elif j=='U':
            c.append(j)
n=len(set(b))
m=len(set(c))
if n==5:
    print('True')
elif m==5:
    print('True')
else:
    print('False')