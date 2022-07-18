x = int(input())
l = list(map(int,input().split()))
a,b=map(int,input().split())
k=[]
for i in l:
    if i>=a and i<=b:
        pass
    else:
        k.append(i)
if k==[]:
    print('-1')
else:
    print(*k)