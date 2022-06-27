n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
for i in range(n):
    if arr[i]>=a and arr[i]<=b:
        s+=arr[i]
print(sum(arr)-s)