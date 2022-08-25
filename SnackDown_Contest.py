x=int(input())
for o in range(x):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    l=[]
    for i in range(1,len(a)):
        if(a[i] not in l):
            l.append(a[i])
    for i in range(1,len(b)):
        if b[i] not in l:
            l.append(b[i])
    if len(l)+1>n:
        print('YES')
    else:
        print('NO')