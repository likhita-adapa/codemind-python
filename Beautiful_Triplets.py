def mi(arr):
    m=1000
    for i in arr:
        if(i<m):
            m=i
    return m
a=int(input())
arr=list(map(int,input().split()))
d=[]
while(len(arr)>=1):
    c=0
    f=0
    m=mi(arr)
    for i in range(len(arr)):
        if(arr[i]-m>=0):
            c+=1
    for i in arr:
        if(i==m):
            f+=1
    for i in range(f):
        arr.remove(m)
    print(c)