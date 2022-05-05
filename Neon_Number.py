n=int(input())
sq=n*n
sum=0
r=0
temp=n
while sq>0:
    r=sq%10
    sum=sum+r
    sq=sq//10
if(sum==temp):
    print("Neon Number")
else:
    print("Not Neon Number")