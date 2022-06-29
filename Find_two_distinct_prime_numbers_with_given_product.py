n=int(input())
l=[]
for i in range(2,n):
    cnt=0
    for j in range(2,i+1):
        if(i%j==0):
            cnt=cnt+1
    if cnt<3:
        l.append(i)
cnt=0
for k in range(len(l)):
    for r in range(k+1,len(l)):
        if l[k]*l[r]==n:
            cnt=cnt+1
            print(l[k],l[r])
if cnt<1:
    print("-1")