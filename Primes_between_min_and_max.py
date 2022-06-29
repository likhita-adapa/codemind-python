def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
a=list(map(int,input().split()))
min=a[0]
max=a[0]
mini=0
maxi=0
for i in range(1,n):
    if max<a[i]:
        max=a[i]
        maxi=i
    if min>a[i]:
        min=a[i]
        mini=i
c=0
if mini<maxi:
    for i in range(mini,maxi+1):
        if prime(a[i]):
            c+=1
else:
    for i in range(maxi,mini+1):
        if prime(a[i]):
            c+=1
print(c)