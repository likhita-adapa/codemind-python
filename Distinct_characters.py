z = input().lower()
l = sorted(set(z))
for i in l:
    if i>='a' and i<='z':
        print(i,end="")