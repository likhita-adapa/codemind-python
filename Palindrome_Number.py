n=int(input())
for i in range(1,n+1,1):
    rg=int(input())
    temp=rg
    s=0
    while(rg>0):
        r=rg%10
        s=(s*10)+r
        rg=rg//10
    if temp==s:
        print('True',end='
')
    else:
        print('False',end='
')