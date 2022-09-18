x=int(input())
y=list(map(int,input().split()))
i=0
s=0
for j in range(x-1,-1,-1):
    s+=(2**i)*y[j]
    i+=1
print(s)