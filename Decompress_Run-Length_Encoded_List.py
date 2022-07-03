n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(0,n,2):
    k=a[i+1]
    for j in range(a[i]):
        l.append(k)
for i in l:
    print(i,end=' ')