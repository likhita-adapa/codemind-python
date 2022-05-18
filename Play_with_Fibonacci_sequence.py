n=int(input())
a=0
c=1
print(a,end=' ')
print(c,end=' ')
for i in range(3,n+1):
    b=a+c
    print(b,end=' ')
    a=c
    c=b