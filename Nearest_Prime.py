def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
x=int(input())
for j in range(x):
    n=int(input())
    temp=n
    for i in range(n,2-1,-1):
        if prime(i):
            p=i
            break
    while temp!=0:
        if prime(temp):
            q=temp
            break
        temp+=1
    if (n-p)<=(q-n):
        print(p)
    else:
        print(q)