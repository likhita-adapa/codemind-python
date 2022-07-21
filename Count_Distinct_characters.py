z = input().lower()
s=set(z)
c=0
for i in s:
    if i>='a' and i<='z':
        c+=1
print(c)