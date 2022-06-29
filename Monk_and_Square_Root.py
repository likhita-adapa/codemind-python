n=int(input())
k=-1
while(n):
    k=-1
    a,b=map(int,input().split())
    for i in range(0,b+1):
        if((i*i)%b==a):
            k=i
            break
    print(k)   
    n=n-1