a = list(map(str,input().lower().split()))
b = list(map(str,input().lower().split()))
s=0
l=[]
m=[]
for i in a:
    if a.count(i)==1:
        l.append(i)
for i in b:
    if b.count(i)==1:
        m.append(i)
for i in l:
    if i in m:
        s+=1
print(s)