x=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
m=[]
for i in l:
    if i>=a and i<=b:
        pass
    else:
        m.append(i)
if m==[]:
    print(-1)
else:
    print(min(m))