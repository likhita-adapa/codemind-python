x=int(input())
l=list(map(int,input().split()))
s,m=0,0
for i in range(x//2):
    s+=l[i]
for i in range(x//2,x):
    m+=l[i]
print(abs(s-m))