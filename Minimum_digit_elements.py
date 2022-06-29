def dig(n):
    if n==0:
        return 1
    c=0
    while(n!=0):
        n=n//10
        c+=1
    return c
n=int(input())
l=[]
a=list(map(int,input().split()))
for i in range(n):
    l.append(dig(a[i]))
x=min(l)
print(l.count(x))