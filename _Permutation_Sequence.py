from itertools import permutations
a,b=map(int,input().split())
l=list(permutations(range(1,a+1)))
for i in l[b-1]:
    print(i,end='')