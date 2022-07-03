n=int(input())
a=list(map(int,input().split()))
s=0
c=0
for i in a:
    s=s+i
avg=s//n
for j in a:
    if j<=avg:
        c+=1
print(c)