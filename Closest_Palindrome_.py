def is_palin(j):
    m = j
    s=0
    while m!=0:
        v = m%10
        s = s*10+v
        m = m//10
    if j==s:
        return j

x = int(input())
for i in range(x-1,1,-1):
    if is_palin(i):
        a = i
        break
g = x+1
while g!=0:
    if is_palin(g):
        b = g
        break
    g+=1
if (x-a)<(b-x):
    print(a)
elif (x-a)==(b-x):
    print(a,b)
else:
    print(b)