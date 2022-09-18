x=int(input())
l=list(map(int,input().split()))
n=sum(l)//len(l)
if n in l:
    print(True)
else:
    print(False)