def prod(a,n):
    if n==1:
        print('0')
        return 
    i=1
    temp=1
    p=[1 for i in range(n)]
    for i in range(n):
        p[i]=temp
        temp*=a[i]
    temp=1
    for i in range(n-1,-1,-1):
        p[i]*=temp
        temp*=a[i]
    for i in range(n):
        print(p[i],end=' ')
        
n=int(input())
a=list(map(int,input().split()))
prod(a,n)
