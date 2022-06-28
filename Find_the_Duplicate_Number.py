n=int(input())
a=list(map(int,input().split()))
count=0
for i in range(len(a)):
    count=0
    for j in range(i+1,n):
        if a[i]==a[j]:
            count+=1
    if count>0:
        print(a[i],end='')