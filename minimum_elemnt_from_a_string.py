s=list(map(str,input().split()))
a=len(s)
s=s[a-1]
n=min(s)
m=n.lower()
if s.count(m)!=0:
    print(m)
else:
    print(n)