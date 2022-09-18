x = int(input())
l = list(map(int,input().split()))
a=[]
b=[]
for i in range(x):
    if l[i]%2==0:
        a.append(l[i])
    else:
        b.append(l[i])
j=0
i=0
while i<len(a) or j<len(b):
    if j<len(b):
        print(b[j],end=" ")
        j+=1
    if i<len(a):
        print(a[i],end=" ")
        i+=1
if x%2==1:
    print('0')