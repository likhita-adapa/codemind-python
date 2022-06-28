n=int(input())
a=list(map(int,input().split()))
count=0
for i in range(len(a)):
    count=0
    for j in range(len(a)):
        if a[j]<a[i]:
            count=count+1
    print(count,end=' ')