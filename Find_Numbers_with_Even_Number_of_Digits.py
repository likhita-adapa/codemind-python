n=int(input())
a=list(map(int,input().split()))
k=0
m=0
r=0
count=0
for i in range(len(a)):
    count=0
    k=a[i]
    while k!=0:
        r=k%10
        count=count+1
        k=k//10
    if(count%2==0):
        m=m+1
print(m)
