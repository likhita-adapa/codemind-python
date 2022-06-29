x = int(input())
l = list(map(int,input().split()))
c=0
if (l[x-2]%2==0 and l[0]%2!=0) or (l[x-2]%2!=0 and l[0]%2==0):
    c+=1
if (l[1]%2==0 and l[x-1]%2!=0) or (l[1]%2!=0 and l[x-1]%2==0):
    c+=1
for i in range(1,len(l)-1):
    if (l[i-1]%2==0 and l[i+1]%2!=0) or (l[i-1]%2!=0 and l[i+1]%2==0):
        c+=1
print(c)