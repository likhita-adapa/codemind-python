x=int(input())
l=list(map(int,input().split()))
c=0
n=sum(l)//len(l)
for i in l:
    if i<=n:
        c+=1
print(c)