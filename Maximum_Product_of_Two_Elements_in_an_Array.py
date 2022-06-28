a=list(map(int,input().split()))
max=0
c=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        c=(a[i]-1)*(a[j]-1)
        if c>max:
            max=c
print(max)