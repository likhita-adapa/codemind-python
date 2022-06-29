x = int(input())
l = list(map(int,input().split()))
m=[]
n=[]
g=[]
for i in range(0,len(l),2):
    m.append(str(l[i]))
for j in range(1,len(l)+1,2):
    n.append(l[j])
b = len(m)
a=0
if a!=b:
    for k in n:
        c = m[a]*k
        g.append(c)
        a+=1
for res in g:
    z = list(res)
    for t in z:
        print(t,end=" ")