n=int(input())
arr=list(map(int,input().split()))
c=0
for i in arr:
    if(i%2!=0):
        c=c+1
if(c<=2):
    print("YES")
else:
    print("NO") 