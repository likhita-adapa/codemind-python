n=int(input())
while n//10!=0:
    sum=0
    while n>0:
        r=n%10
        sum=sum+r
        n=n//10
    n=sum
print(sum)