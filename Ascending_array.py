x = int(input())
l = list(map(int,input().split()))
c=0
for i in range(1,x):
    if l[i-1]<l[i]:
        c+=1
if c==x-1:
    print('yes')
else:
    print('no')