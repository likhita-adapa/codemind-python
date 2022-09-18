x = int(input())
l = list(map(str,input().split()))
c=0
for i in l:
    for j in i:
        c+=int(j)
print(c)