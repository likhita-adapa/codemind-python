x = list(map(str,input().lower().split()))
y = list(map(str,input().lower().split()))
s=0
for i in x:
    if i in y:
        s+=1
print(s)