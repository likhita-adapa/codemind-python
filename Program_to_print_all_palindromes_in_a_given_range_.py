a=int(input())
b=int(input())
for i in range(a,b+1):
    temp=i#1,2,3,4,5,6,7
    f=temp
    r=0
    while(temp>0):
        rem=temp%10
        r=(r*10)+rem;
        temp=temp//10
    if f==r:
        print(f,end=' ')