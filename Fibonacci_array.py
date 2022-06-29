x = int(input())
l = list(map(int,input().split()))
c=0
for i in range(2,x):
    if l[i-1]+l[i-2]==l[i]:
       c=1
    else:
        c=0
        break
if c==0:
    print('no')
else:
    print('yes')