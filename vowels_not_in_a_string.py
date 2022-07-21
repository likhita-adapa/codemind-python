x=input().lower()
l = ['a','e','i','o','u']

for i in set(x):
    if i>='a' and i<='z':
        if i in l:
            l.remove(i)
            
if len(l)==0:
    print('0')
else:
    print(*l)