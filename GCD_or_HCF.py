i,j=map(int,input().split())
while(i!=j):
  if(i>j):
     i=i-j
  else:
     j=j-i
print(i)