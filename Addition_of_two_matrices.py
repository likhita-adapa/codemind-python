n=int(input())
s=[0]*(n*n)
a=[]
b=[]
for j in range(2):
    for l in range(n):
        m=list(map(int,input().split()))
        if j==0:
            for h in m:
                a.append(h)
        if j==1:
            for g in m:
                b.append(g)
for k in range(n*n):
    if k%n==(n-1):
        print(a[k]+b[k])
    else:
        print(a[k]+b[k],end=' ')