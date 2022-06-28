n=int(input())
a=list(map(int,input().split()))
c=0
max=0
s=0
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if i!=j:
            if a[i]==a[j]:
                c=c+1
    if c==0 and a[i]>max:
        max=a[i]
        s=s+1
if s>0:
    print(max)
else:
    print("-1")