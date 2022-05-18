n=int(input())
c=0
d=0
for i in range(1,n+1):
   if(n%i==0):
      c=0
      for x in range(1,i+1):
        if(i%x==0):
           c+=1
      if(c!=2):
         d+=1
print(d)