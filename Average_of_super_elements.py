n=int(input())
a=list(map(int,input().split()))
s=0
l=[]
for i in sorted(set(a),key=a.index):
    if a.count(i)==i:
        l.append(i)
if l==[]:
    print('-1')
else:
    avg=sum(l)/len(l)
    print('%.2f'%avg)