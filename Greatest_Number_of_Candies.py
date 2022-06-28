n=int(input())
a=list(map(int,input().split()))
x=int(input())
max=0
for i in range(len(a)):
    if a[i]+x>=max:
        max=a[i]
        print("True",end=' ')
    else:
        print("False",end=' ')
        