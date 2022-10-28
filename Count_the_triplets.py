for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(len(a)):
        for j in range(i,len(a)):
            if i!=j:
                p=a[i]+a[j]
                if p in a:
                    c+=1
    if c==0:
        print('-1')
    else:
        print(c)