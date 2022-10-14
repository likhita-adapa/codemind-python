x = list(map(str,input().split()))
b=[]
for i in x:
    b.append(len(str(i)))
print(min(b))