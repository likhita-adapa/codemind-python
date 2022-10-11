t=int(input())
while(t):
    n=int(input())
    binn=n
    dec=0
    b=0
    while n:
        r=n%10
        dec+=r*(2**b)
        b+=1
        n=n//10
    oct=0
    i=1
    while dec:
        oct+=(dec%8)*i
        i=i*10
        dec=dec//8
    print(oct)    
    t-=1