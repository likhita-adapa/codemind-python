n=3
a=list(map(int,input().split()))
m=3
b=list(map(int,input().split()))
c=0
d=0
for i in range(0,3):
    if a[i]>b[i]:
        c=c+1
    elif a[i]<b[i]:
        d=d+1
print(c,end=" ")
print(d,end=" ")