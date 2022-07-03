a=int(input())
p="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s=""
while a>0:
    r=a%26
    if r==0:
        s+='Z'
        a=(a//26)-1
    else:
        s+=p[r-1]
        a//=26
for i in range(len(s)-1,-1,-1):
    print(s[i],end="")