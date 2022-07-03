n=int(input())
a=list(map(int,input().split()))
s=0
c=0
for i in range(0,n//2):
    s=s+a[i]
print(s)
for j in range((n//2),n):
    c+=a[j]
print(c)