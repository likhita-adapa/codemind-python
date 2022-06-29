n=int(input())
v=0
p=0
m=0
for i in range(1,n+1,1):
    if(n%i==0):
        v+=1
if(v!=2):
    print("Not Mega Prime")
else:
    while(n>0):
        k=0
        r=n%10
        for j in range(1,r+1,1):
            if(r%j==0):
                k+=1
        if(k==2):
            m+=1
        n=n//10
        p+=1
    if(p==m):
        print('Mega Prime')
    else:
        print('Not Mega Prime')