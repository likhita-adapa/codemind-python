x=int(input())
y=int(input())
s=0
for i in range(x):
    l=list(map(int,input().split()))
    s+=sum(l)
print(s)