def solve(n,d,x):
    if x==n:
        print(d,end=' ')
        return 
    for i in range(1,10):
        if d%10<i:
            solve(n,d*10+i,x+1)
n=int(input())
if n==1:
    print(0,end=' ')
solve(n,0,0)