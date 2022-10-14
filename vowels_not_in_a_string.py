s=input()
v='aeiou'
l=[]
c=0
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        l.append(i)
if len(set(l))==len(set(v)):
    print(0)
else:
    for j in v:
        for k in list(set(l)):
            if j==k:
                c+=1
        if c==0:
            print(j,end=' ')
        c=0