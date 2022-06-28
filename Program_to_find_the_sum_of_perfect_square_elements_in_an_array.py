n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range(0,len(a)):
    k=a[i]
    for j in range(1,a[i]+1):
        m=j*j
        if k==m:
            sum=sum+k
            break
print(sum)
        