n=int(input())
a=list(map(int,input().split()))
even=0
odd=0
x=0
for i in range(len(a)):
    if i%2==0:
        even=even+a[i]
    elif i%2!=0:
        odd=odd+a[i]
x=even-odd
if x==0:
    print("YES")
else:
    print("NO")