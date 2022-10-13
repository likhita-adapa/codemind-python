s=list(map(str,input().split()))
c=0
for i in s:
    m=i.lower()
    n=m[::-1]
    if m==n:
        c+=1

print(c)