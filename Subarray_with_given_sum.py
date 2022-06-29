def subarr(n,m,a):
    for i in range(n):
        s=a[i]
        for j in range(i+1,n+1):
            if s==m:
                print("%d %d"%(i+1,j))
                return 1
            if s>m or j==n:
                break
            s=s+a[j]
    print('-1')
    return 0
x=int(input())
for i in range(x):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    subarr(n,m,a)