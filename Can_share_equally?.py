x,y=map(int,input().split())
c=x+y*2
if x==0 and y%2==0:
    print("YES")
elif x==0 and y%2!=0:
    print("NO")
elif c%2==0:
    print("YES")
else:
    print("NO")