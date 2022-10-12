s=input().lower()
s=s.split()
s1=''
l=list(s[0])
s.remove(s[0])
f=0
for i in l:
    for j in s:
        if i not in j:
            f=1
            break
    else:
        s1+=i
        
if len(s1)==0:
    print(-1)
else:
    print(s1)