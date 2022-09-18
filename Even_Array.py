x=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    if i%2==0:
        s+=1
if s==len(l):
    print(True)
else:
    print(False)