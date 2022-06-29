def dig(n):
    c=0
    while n:
        i=n%10
        n=n//10
        c+=1
    return c
n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(n):
    l.append(dig(a[i]))
x=max(l)
print(l.count(x))