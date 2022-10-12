z = input().lower()
s=0
for i in sorted(z):
    if i>='a' and i<='z':
        if z.count(i)==1:
            s+=1
print(s)