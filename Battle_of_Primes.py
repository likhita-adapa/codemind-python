def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
a=int(input())
b=int(input())
for i in range(1,100):
    c=a+b+i
    if(prime(c)):
        print(i)
        break