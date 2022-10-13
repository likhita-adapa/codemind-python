x = list(map(str,input().split()))
c=0
l = ['a','e','i','o','u','A','E','I','O','U']
for i in x:
    n = len(i)
    if (i[0] in l) and (i[n-1] not in l):
        c+=1
print(c)