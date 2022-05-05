n=int(input())
r=0
sum=0
x=n
while n!=0:
    r=n%10
    sum=sum*10+r
    n=n//10
if sum==x:
    print("True")
else:
    print("False") 