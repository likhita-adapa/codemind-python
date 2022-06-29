m=int(input())
n=int(input())
c=0
for i in range(m,n+1):
    if i==1:
        continue
    else:
        c=0
        for j in range(2,i):
            if i%j==0:
                c+=1
        if c==0:
            print(i)