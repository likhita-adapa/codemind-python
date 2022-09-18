x = int(input())
l = list(map(int,input().split()))
a,b=map(int,input().split())
s=0
for i in l:
    if i>=a and i<=b:
        s+=i
print(s)