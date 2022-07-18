x = int(input())
l = list(map(int,input().split()))
a,b=map(int,input().split())
n=[]
for i in l:
    if i>=a and i<=b:
        pass
    else:
        n.append(i)
if n==[]:
    print('-1')
else:
    print(max(n))