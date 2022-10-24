n=int(input())
for j in range(n):
    a,b,c,d=map(int,input().split())
    x=a//b
    y=a%b
    s=0
    for i in range(x):
        s+=(c+i*d)*b
    s+=(c+x*d)*y
    print(s)
