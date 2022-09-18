x = int(input())
l = list(map(int,input().split()))
for i in l:
    if i<0:
        i = i*-1
        s=0
        while i!=0:
            n = i%10
            s = s*10+n
            i//=10
        print('-',end="")
        print(s,end=" ")
        s=0
    else:
        s=0
        while i!=0:
            n = i%10
            s = s*10+n
            i//=10
        print(s,end=" ")
        s=0