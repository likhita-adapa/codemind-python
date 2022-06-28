s=input()
x=s.split(' ')
l=[]
for i in x:
    l.append(len(i))
print(max(l))