x = int(input())
l=list(map(int,input().split()))
c=0
for i in range(x-1):
    if l[i]>l[i+1]:
        c+=1
if c==x-1:
    print('yes')
else:
    print('no')