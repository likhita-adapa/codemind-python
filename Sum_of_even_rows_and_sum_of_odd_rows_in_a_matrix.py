x , y = map(int,input().split())
s=0
c=0
for i in range(x):
    if i%2==0:
        l = list(map(int,input().split()))
        s += sum(l)
    else:
        l = list(map(int,input().split()))
        c += sum(l)
print(s,end=" ")
print(c)