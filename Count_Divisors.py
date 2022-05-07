i,r,s=map(int,input().split())
c=0
for i in range(i,r+1,1):
    if(i%s==0):
        c=c+1
print(c)         