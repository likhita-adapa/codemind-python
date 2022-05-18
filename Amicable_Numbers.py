n1=int(input())
n2=int(input())
a=0
for i in range(1,(n1//2)+1,1):
    if(n1%i==0):
        a=a+i
b=0
for i in range(1,(n2//2)+1,1):
    if(n2%i==0):
        b=b+i
if(a==n2 and b==n1):
    print("Amicable")
else:
    print("Not Amicable")