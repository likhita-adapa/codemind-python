s=input()
c=0
c1=0
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        if c1<c:
            c1=c
        c=0
if c1<c:
    c1=c
print(c1+1)