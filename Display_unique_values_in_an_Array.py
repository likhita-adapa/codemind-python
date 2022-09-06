import math
n=int(input())
p=list(map(int,input().split()))
v=0
c=0
r=0
k=0
b=[]
for i in range(n):
    c=0
    for j in range(n):
        if(i!=j):
            if(p[j]==p[i]):
                c+=1
    if(c==0):
        print(p[i],end=" ")
        k+=1
if(k==0):
    print("-1")