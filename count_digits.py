def dig(n):
    if n==0:
        return 1
    if n<0:
        n=n*-1
    c=0
    while n:
        i=n%10
        n=n//10
        c+=1
    return c
n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    print(dig(a[i]),end=' ')