n,m=map(int,input().split())
a=list(map(int,input().split()))
c=s=0
for i in range(n):
    for j in range(i,n):
        s=s+a[j]
        if s==m:
            c+=1
        if s>m:
            break
    s=0
print(c)
