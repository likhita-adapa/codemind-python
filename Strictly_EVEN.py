n=int(input())
a=list(map(int,input().split()))
c=0
d=0
for i in range(n):
    if i%2==0 and a[i]%2==0:
        c+=1
    if a[i]%2==0:
        d+=1
if c==d:
    print('True')
else:
    print('False')