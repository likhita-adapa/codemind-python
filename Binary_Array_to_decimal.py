n=int(input())
a=list(map(int,input().split()))
j=0
c=0
for i in range(n-1,-1,-1):
    c+=(a[i]*(2**j))
    j+=1
print(c)