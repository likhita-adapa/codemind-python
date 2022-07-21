x = input().lower()
y = input().lower()
x = set(x)
y = set(y)
s=0
for i in x:
    if i!=' ':
        if i in y:
            s+=1
print(s)