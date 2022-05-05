n=int(input())
num=n
rem=sum=0
while(num>0):
    rem=num%10
    sum=sum+rem
    num=num//10
if n%sum==0:
    print("True")
else:
    print("False")