
x = input().lower()
y = input().lower()
l=[]
c=0
for i in x:
    if i in y:
        l.append(i)
for j in sorted(set(l)):
    if j!=' ':
        c+=1
print(c)