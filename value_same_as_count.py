x=int(input())
l=list(map(int,input().split()))
c=0
for i in set(l):
    if i==l.count(i):
        c+=1
print(c)