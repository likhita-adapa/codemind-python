n=int(input())
a=list(map(int,input().split()))
for i in a:
    if i%2==0:
        print(i,end=' ')
for j in a:
    if j%2!=0:
        print(j,end=' ')