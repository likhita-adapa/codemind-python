n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    c=0
    for j in range(i+1,n):
        c+=1
        if a[i]<a[j]:
            print(c,end=' ')
            break
    else:
        print('0',end=' ')
