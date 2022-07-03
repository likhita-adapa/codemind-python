n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
ans=[None]
for i in range(n):
    ans.insert(b[i],a[i])
for i in range(n):
    print(ans[i],end=' ')