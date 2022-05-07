n=int(input())
a=0
b=0
while(n>0):
    r=n%10
    if(r%2==0):
        a=a+1
    else:
        b=b+1
    n=n//10
if(a>0 and b>0):
    print("Mixed")
elif(a>0 and b==0):
    print("Even")
else:
    print("Odd")
    