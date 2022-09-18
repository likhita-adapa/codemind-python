x = int(input())
l = list(map(int,input().split()))
a,b=map(int,input().split())
k=[]
for i in range(x):
    if l[i]>=a and l[i]<=b:
        k.append(l[i])
if k==[]:
    print('-1')
else:
    print(min(k))