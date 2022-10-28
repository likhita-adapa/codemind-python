z=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
s=[]
for i in range(z):
    s.append(a[i]+b[i])
print(*s)