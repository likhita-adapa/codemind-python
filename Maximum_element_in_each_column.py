n,m=map(int,input().split())
l=[]
k=[]
s=[]
p=[]
x=[]
for i in range(n):
    a=list(map(int,input().split()))
    l.append(a[0])
    k.append(a[1])
    if m>2:
        s.append(a[2])
    if m>3:
        p.append(a[3])
    if m>4:
        x.append(a[4])
print(max(l))
if m>=2:
    print(max(k))
if m>=3:
    print(max(s))
if m>=4:
    print(max(p))
if m>=5:
    print(max(x))
