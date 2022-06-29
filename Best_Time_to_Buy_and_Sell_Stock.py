n=int(input())
a=list(map(int,input().split()))
x=0
for i in range(n):
    for j in range(i,n):
        if x<a[j]-a[i]:
            x=a[j]-a[i]
print(x)