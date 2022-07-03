from itertools import *
x = input()
b=[]
e=[]
c=0
for i in x:
    if i.isdigit():
        b.append(int(i))
        c=1
b = sorted(set(b),key=b.index)
b = sorted(b,reverse=True)
for i in b:
    if i%2==0:
        e.append(i)
if c==0:
    print('-1')
elif e==[]:
    print('-1')
else:
    l = min(e)
    for i in range(len(b)):
        if b[i]==l:
            m=i
    b[len(b)-1],b[m]=b[m],b[len(b)-1]
    for i in b:
        print(i,end="")