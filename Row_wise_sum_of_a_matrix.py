x , y = map(int,input().split())
c=[]
d=[]
for i in range(x):
    l = list(map(int,input().split()))
    d.append(sum(l))
print(*d)