def palin(i):
    s = str(i)
    m = s[::-1]
    if m==s:
        return 1
n = int(input())
a = list(map(int,input().split()))
c=0
for i in a:
    if palin(i):
        c+=1
print(c)