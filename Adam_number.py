n=int(input())
sqr=n*n
temp=n
s=0
r=0
prod=0
sum=0
while temp>0:
    r=temp%10
    sum=sum*10+r
    temp=temp//10
s=sum*sum
while s>0:
  r=s%10
  prod=prod*10+r
  s=s//10
if sqr==prod:
    print("True")
else:
    print("False")