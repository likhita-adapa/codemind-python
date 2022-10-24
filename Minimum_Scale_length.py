n=int(input())
l=list(map(int,input().split(" ")))
ml=min(l)
j=1
c=0
m=0
while True:
    j+=1
    if j>ml:
        break
    elif j<=ml:
        k=0
        for i in l:
            if i%j==0:
                k+=1
        if k==len(l):
            m=j
            c=1
if c==0:
    print(1)
else:
    print(m)
    