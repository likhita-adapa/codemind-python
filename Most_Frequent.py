n=int(input())
a=list(map(int,input().split()))
m=0
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if a[i]==a[j]:
           c=c+1
    if c>m:
        m=c
        k=a[i]
    elif c==m and a[i]<k:
        k=a[i]
print(k)