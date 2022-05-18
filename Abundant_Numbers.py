n=int(input())
j=0
for i in range(1,n//2+1,1):
    if n%i==0:
        j=j+i
if(j>n):
    print('True')
else:
    print('False')