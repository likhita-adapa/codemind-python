x = input()
l=[]
for i in x:
    if i.isalnum():
        l.append(i)
n = max(l)
m=min(l)
print(m,end=" ")
print(l.count(m),end=" ")
print(n,end=" ")
print(l.count(n))