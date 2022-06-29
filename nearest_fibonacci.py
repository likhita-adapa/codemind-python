def fib(n):
    a=0
    b=1
    c=a+b
    while c<n:
        c=a+b
        a=b
        b=c
    if c==n:
        return 1
    return 0
n=int(input())
temp=n
for i in range(n,0,-1):
    if fib(i):
        p=i
        break
while temp!=0:
    if fib(temp):
        q=temp
        break
    temp+=1
if (n-p)<(q-n):
    print(p)
elif (n-p)==(q-n):
    print(p,q)
else:
    print(q)