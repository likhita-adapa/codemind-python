x1=input().lower()
x2=input().lower()
l,s,m=[],[],[]
for i in x1:
    if i.isalnum():
        l.append(i)
for i in x2:
    if i.isalnum():
        s.append(i)
for i in l:
    if i not in s:
        m.append(i)
for i in s:
    if i not in l:
        m.append(i)
m=set(m)
print(len(m))