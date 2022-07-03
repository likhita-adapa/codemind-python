x=int(input())
l=0
for i in range(x):
    l+=1
    n=int(input())
    c=0
    a=list(map(int,input().split()))
    for j in range(n):
        ans1=ans2=-1
        if j==0:
            if a[j]>a[j+1]:
                c+=1
        else:
            for k in range(j):
                if a[k]>a[j]:
                    ans1=1
                    break
                elif a[k]<a[j]:
                    ans1=0
            if j==(n-1):
                if ans1==0:
                    c+=1
            else:
                if a[j]>a[j+1]:
                    ans2=1
                if ans1==0 and ans2==1:
                    c+=1
    print('Case #',end='')
    print(l,end='')
    print(':',end=' ')
    print(c)