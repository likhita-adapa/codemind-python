t=int(input())
c=0
while t>0:
    n=int(input())
    c=0
    for i in range(1,n+1):
        if i*i==n:
            c+=1
    if c>0:
        print("True")
    else:
        print("False")
    t=t-1