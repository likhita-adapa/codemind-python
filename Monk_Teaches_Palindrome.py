t=int(input())
x=0
while t>0:
    s=input()
    x=s[::-1]
    if s==x:
        print("YES",end=' ')
        if len(s)%2==0:
            print('EVEN')
        else:
            print('ODD')
    else:
        print('NO')
    t=t-1