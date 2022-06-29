def prime(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            return False
    if c==0:
        return True
n=int(input())
x=0
for i in range(1,n):
    if prime(i):
        for j in range(1,n):
            if prime(j):
                if i*j==n:
                    x=1
                    print(i,end=' ')
                    print(j,end=' ')
    if x==1:
        break

if x==0:
    print("-1")
        