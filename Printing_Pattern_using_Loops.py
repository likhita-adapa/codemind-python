n=int(input())
k=n
m=n+n-1
for i in range(m):
    for j in range(m):
        if i<=n-1:
            if i==0:
                print(k,end=' ')
            if i>=1:
                if j<i:
                    print(k-j,end=' ')
                elif j>=i and j<m-i:
                    print(k-i,end=' ')
                else:
                    print((j-k+1)+1,end=' ')
        elif i==n-1:
            if j<n:
                print(k-j,end=' ')
            else:
                print((j-k+1)+1,end=' ')
        elif i>=n:
            x=m-i-1
            if i==m:
                print(m,end=' ')
            if j<x:
                print(k-j,end=' ')
            elif j>=x and j<m-x:
                print(k-x,end=' ')
            else:
                print((j-k+1)+1,end=' ')
    print()