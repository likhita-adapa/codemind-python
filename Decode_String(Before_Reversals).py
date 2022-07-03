n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    s=input()
    while(y>0):
        l=s[:y]
        s=l[::-1]+s[y:]
        y-=1
    print(s)