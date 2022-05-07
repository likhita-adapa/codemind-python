n=int(input())
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if(i+j==n+1 or i==j):
            print("x",end="")
        else:
            print("0",end="")
    print()               