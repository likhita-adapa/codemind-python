def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
x=int(input())
l=list(map(int,input().split()))
c=0
a=int(input())
for i in l:
    if i<=a:
        if prime(i):
            c+=1
print(c)