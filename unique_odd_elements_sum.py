n=int(input())
a=list(map(int,input().split()))
a=set(a)
s=0
for i in set(a):
    if i%2!=0:
        s+=i
print(s)
