x=int(input())
l=list(map(int,input().split()))
a=[]
for i in sorted(set(l),key=l.index):
    if i==l.count(i):
        a.append(i)
if a==[]:
    print('-1')
else:
    print(*a)