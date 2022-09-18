x=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if i==l.count(i):
        a.append(i)
if a==[]:
    print('-1')
else:
    print(min(a),end=' ')
    print(max(a),end=' ')