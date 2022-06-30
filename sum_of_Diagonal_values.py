n,m=map(int,input().split())
s=0
for i in range(n):
    a=list(map(int,input().split()))
    for j in range(len(a)):
        if j==i or j==len(a)-1-i:
            s=s+a[j]
print(s)