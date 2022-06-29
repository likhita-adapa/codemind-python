n=int(input())
c=0
s=0
for i in range(1,n+1):
    if(n%i==0):
        c+=1
if(c!=2):
    print('not prime')
else:
    while(n>0):
        r=n%10
        s=s*10+r
        n=n//10
    c=0
    for i in range(1,s+1):
        if(s%i==0):
            c+=1
    if(c==2):
        print("circular prime")
    else:
        print("prime but not a circular prime")