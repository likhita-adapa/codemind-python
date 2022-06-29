a,b=map(int,input().split(':'))
v=abs(30*a-((11/2)*b))
d=360-v
if v<d:
    print(v)
else:
    print(d)