n=int(input())
a=list(map(int,input().split()))
x=list(set(a))
l=[]
c=0
for i in range(len(x)):
    for j in range(len(a)):
        if x[i]==a[j]:
            c+=1
    l.append(c//2)
    c=0
print(sum(l))