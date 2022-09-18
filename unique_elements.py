x=int(input())
l=list(map(int,input().split()))
l=sorted(set(l),key=l.index)
print(*l)