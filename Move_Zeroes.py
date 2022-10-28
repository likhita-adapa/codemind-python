x = int(input())
l = list(map(int,input().split()))
n=[]
m=[]
for i in l:
    if i==0:
        n.append(i)
    else:
        m.append(i)
for j in m:
    print(j,end=" ")
for k in n:
    print(k,end=" ")
