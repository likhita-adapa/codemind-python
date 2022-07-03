s=input()
u,d,l,r=0,0,0,0
for i in s:
    if i=='U':
        u+=1
    if i=='D':
        d+=1
    if i=='L':
        l+=1
    if i=='R':
        r+=1
if u==d and r==l:
    print('True')
else:
    print('False')