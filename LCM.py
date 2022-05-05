x,y=map(int,input().split())
g=0
if x>y:
    g=x
else:
    g=y
    while 1:
        if g%x==0 and g%y==0:
            lcm=g
            print(lcm)
            break
        g+=1