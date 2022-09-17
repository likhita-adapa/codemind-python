a,b,c,d=map(int,input().split())
for i in range(a,b+1):
    for j in range(c,d+1):
        p=i+j
        for k in range(2,p):
            if p%k==0:
                break
        else:
            break
    else:
        print('Takahashi')
        exit()
else:
    print('Aoki')