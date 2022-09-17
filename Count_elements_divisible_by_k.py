x,y = map(int,input().split())
l = list(map(int,input().split()))
c=0
for i in l:
    if i%y==0:
        c+=1
print(c)