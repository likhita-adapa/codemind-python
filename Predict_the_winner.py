n=int(input())
a=list(map(int,input().split()))
even=0
odd=0
k=0
for i in range(len(a)):
    if i%2==0:
        even=even+a[i]
    elif i%2!=0:
        odd=odd+a[i]
k=even-odd
if k%4==0:
    print("X")
else:
    print("Y")