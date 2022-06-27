n=int(input())
a=list(map(int,input().split()))
if n%2==0:
    print(*a)
if n%2!=0:
    for i in a:
        print(i,end=' ')
    print('0')