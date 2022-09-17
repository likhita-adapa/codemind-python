x,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
for i in set(a):
    if i in b:
        c+=1

print(c)