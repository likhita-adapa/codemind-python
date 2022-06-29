n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
s=0
s1=0
for i in a:
    if i==-1:
        c+=1
    else:
        s+=i
for i in b:
    if i==-1:
        c+=1
    else:
        s1+=i
if c==2:
    print('Infinite')
else:
    c1=0
    for i in range(9999):
        if i+s==s1:
            c1+=1
    print(c1)
