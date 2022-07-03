n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
k=[]
c=0
for i in l:
    if i>=a and i<=b:
        pass
    else:
        k.append(i)
        c=1
if c==0:
    print('-1')
else:
    print(min(k))