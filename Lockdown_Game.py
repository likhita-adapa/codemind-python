n=int(input())
l=[]
for i in range(1,n+1):
    l.append(i)
s=input()
i=0
j=0
while (len(l)!=1):
    if s[i]=='y':
        l.pop(j)
        i+=1
    else:
        i+=1
        j+=1
    if (i>len(s)-1):
        i=0
    if (j>len(l)-1):
        j=0
print(*l)