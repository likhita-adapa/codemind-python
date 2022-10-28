n=int(input())
a=list(map(int,input().split()))
maxx=-1000
for p in range(n):
    f=a[0]
    a[0]=a[n-1]
    for k in range(1,n):
        temp=a[k]
        a[k]=f
        f=temp  
    for i in range(n):
        s=0
        for j in range(i,n):
            s+=a[j]
            if maxx<s:
                maxx=s
print(maxx)