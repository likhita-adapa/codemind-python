x = list(map(str,input().split()))
b=[]
for i in x:
    b.append(len(i))
print(max(b))