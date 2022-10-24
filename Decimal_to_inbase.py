n=int(input())
m=int(input())
l=[]
while(n>0):
    i=n%m
    l.append(i)
    n=n//m
c=0
max=0
for i in range(len(l)):
    c=0
    for j in range(i,len(l)):
        if l[j]==0:
            c+=1
            if max<c:
                max=c
        else:
            break
if max==0:
    print(-1)
else:
    print(max)
    
    
    
    
    
    
    
    
    
    
    
    