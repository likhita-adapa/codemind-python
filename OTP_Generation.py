n=int(input())
sum=0
k=[]
while n!=0:
    r=n%10
    k.append(r)
    n=n//10
k=k[::-1]
for i in range(len(k)):
    if k[i]%2==0:
        continue
    elif k[i]%2!=0:
        x=k[i]*k[i]
        print(x,end='')