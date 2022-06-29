def maxsubarr(a,size):
    s=a[0]
    cm=a[0]
    for i in range(1,size):
        cm=max(a[i],cm+a[i])
        s=max(s,cm)
    return s
n=int(input())
a=list(map(int,input().split()))
print(maxsubarr(a,n))
