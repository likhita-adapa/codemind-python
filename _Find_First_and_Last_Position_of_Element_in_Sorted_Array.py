n=int(input())
a=list(map(int,input().split()))
k=int(input())
c=0
d=0
for i in range(0,n):
    if a[i]==k:
        print(i,end=' ')
        c=1
        break
if c==0:
    print("-1",end=' ')
for j in range(n-1,-1,-1):
    if a[j]==k:
        print(j,end='')
        d=1
        break
if d==0:
    print("-1",end=' ')