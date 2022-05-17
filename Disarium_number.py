n=int(input())
I=0
t=n
while n:
    I+=1
    n=n//10
n=t
v=0
while n:
    r=n%10
    v=v+pow(r,I)
    n=n//10
    I-=1
if v==t:
    print('True')
else:
    print('False')