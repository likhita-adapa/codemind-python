def dig(n):
    c=0
    if n==0:
        return 1
    elif n<0:
        n = n*-1
    while(n):
        n=n//10
        c+=1
    return c
x , y = map(int,input().split())
l = list(map(int,input().split()))
a=[]
for i in range(x):
   a.append(dig(l[i]))
print(a.count(y))