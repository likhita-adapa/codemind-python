n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    if i==1 or i==0:
        s=1
    else:
        s=0
if s==1:
    print('True')
else:
    print('False')