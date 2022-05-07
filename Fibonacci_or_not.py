n=int(input())
n1=0
n2=1
n3=0
j=0
for i in range(1,1+n,1):
    n1=n2
    n2=n3
    n3=n1+n2
    if(n3==n):
        j=j+1
if j==0:
    print("False")
else:
    print("True")   