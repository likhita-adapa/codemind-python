t=int(input())
for l in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    f=0
    for i in range(n):
        l=sum(arr[:i])
        r=sum(arr[i+1:])
        if l==r:
            f=1
            break
    if l==r:
        print("YES")
    else:
        print("NO")