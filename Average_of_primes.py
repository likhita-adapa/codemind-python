def prime(n):
    if n==1:
        return 0
    for i in range(2,(n//2)+1):
        if n%i==0:
            return 0
    return 1
x = int(input())
l = list(map(int,input().split()))
b=[]
for i in l:
    if prime(i):
        b.append(i)
print(format(sum(b)/len(b),".2f"))