n=int(input())
l=list(map(int,input().split()))
d=2
while True:
    c=0
    for i in l:
        if d%i==0:
            c+=1
    if len(l)==c:
        print(d)
        break
    d+=1