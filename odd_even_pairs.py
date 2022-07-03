n=int(input())
a=list(map(int,input().split()))
l=[]
k=[]
for i in range(n):
    if a[i]%2==0:
        l.append(a[i])
    else:
        k.append(a[i])
i=0
j=0
while i<len(l) or j<len(k):
    if j<len(k):
        print(k[j],end=' ')
        j+=1
    if i<len(l):
        print(l[i],end=' ')
        i+=1
if n%2!=0:
    print('0')