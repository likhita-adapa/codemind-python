x=int(input())
l=list(map(int,input().split()))
a=int(input())
b=[]
for i in set(l):
    if l.count(i)==a:
        b.append(i)
if b==[]:
    print('-1')
else:
    print(*b)