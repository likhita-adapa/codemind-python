n=int(input())
peo=[]
hou=[]
for i in range(n):
    a=int(input())
    peo.append(a)
for i in range(n):
    a=int(input())
    hou.append(a)
c=0
count=0
for i in range(n):
    c=1
    for j in range(n):
       if(peo[i]<=hou[j]):
          hou[j]=0
          c=0
          break
    if(c!=0):
        count+=1
print(count)