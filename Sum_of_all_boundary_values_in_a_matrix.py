n,x=map(int,input().split())
s=0
for j in range(n):
    m=list(map(int,input().split()))
    for i in range(len(m)):
        if j==0 or j==(n-1):
            s=s+m[i]
        else:
            if i==0 or i==(len(m)-1):
                s=s+m[i]
print(s)