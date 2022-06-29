n,m=map(int,input().split())
s=[0]*m
for j in range(n):
    m=list(map(int,input().split()))
    for i in range(len(m)):
        s[i]=s[i]+m[i]
print(max(s))