x = eval(input())
f = 0
if x ==1:
    print("prime")
for i in range(2,x+1):
    if x%i==0:
        f+=1
if f==1:
    print("prime")
else:
    print("not a prime")