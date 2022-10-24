x = input()
c,s=0,0
l=[]
for i in list(set(x)):
    for j in x:
        if i==j:
            c+=1
    if c==1:
        s+=1
    else:
        l.append([c,i])
    c=0
n = max(l)
m = min(l)
b = (m[0]-n[0])
if s>1:
    print('Not Valid')
else:
    if b==0 or b==1:
        print('Valid String')
    else:
        print('Not Valid')

