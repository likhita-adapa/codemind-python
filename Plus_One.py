n=int(input())
num=0
l=list(map(int,input().split()))
for i in range(n):
    num=num*10+l[i]
arr=[]
num+=1
s=0
while num!=0:
    r=num%10
    arr.append(r)
    s+=1
    num//=10
for i in range(s-1,-1,-1):
    print(arr[i],end=' ')