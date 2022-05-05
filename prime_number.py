n=int(input())
c=1
for i in range(2,n):
    if n%i==0:
        c=0
if c==1:
    print("prime")
else:
    print("not a prime")  