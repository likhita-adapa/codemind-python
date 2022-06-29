n=int(input())
a=list(map(int,input().split()))
l=[]
if n%2!=0:
    for i in range(n//2+1):
        if i!=(n-1)-i:
            print(a[i],end=' ')
            print(a[(n-1)-i],end=' ')
    print(a[i],end=' ')
    print('0')
elif n%2==0:
    for i in range(n//2):
        if i!=(n-1)-i:
            print(a[i],end=' ')
            print(a[(n-1)-i],end=' ')