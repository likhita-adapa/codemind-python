n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
for i in sorted(set(a),key=a.index):
    if b.count(i)!=0:
        print(i,end=' ')