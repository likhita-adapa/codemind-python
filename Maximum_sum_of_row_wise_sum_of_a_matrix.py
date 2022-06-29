n,m=map(int,input().split())
s=0
a=[]
for j in range(n):
    m=list(map(int,input().split()))
    for i in range(len(m)):
        s=s+m[i]
    a.append(s)
    s=0
print(max(a))