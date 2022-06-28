n=int(input())
a=list(map(int,input().split()))
m=0
for i in range(len(a)):
    count=0
    for j in range(len(a)):
        if a[i]==a[j]:
            count=count+1
        if count>m:
            m=count
            k=a[i]
print(k)