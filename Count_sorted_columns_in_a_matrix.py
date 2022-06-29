n,m=map(int,input().split())
c=0
p=[]
for l in range(m):
    p.append([])
for i in range(n):
    a=list(map(int,input().split()))
    for j in range(m):
        p[j].append(a[j])
for k in p:
    b=k.copy()
    b.sort()
    q=b[::-1]
    if k==b or k==q:
        c+=1
print(c)