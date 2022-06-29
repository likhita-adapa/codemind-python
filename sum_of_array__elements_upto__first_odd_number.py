n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(n):
    if(a[i]%2!=0):
        break
    s+=a[i]
print(s)