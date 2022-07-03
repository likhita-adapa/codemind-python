n=int(input())
a=list(map(int,input().split()))
c,c1=0,0
for i in range(n):
    if i%2!=0 and a[i]%2!=0:
        c+=1
    if a[i]%2!=0:
        c1+=1
if c==c1:
    print('True')
else:
    print('False')