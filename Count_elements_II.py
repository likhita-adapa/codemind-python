n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
for i in list(set(a)):
    if b.count(i)==0:
        c+=1
for j in list(set(b)):
    if a.count(j)==0:
        c+=1
print(c)