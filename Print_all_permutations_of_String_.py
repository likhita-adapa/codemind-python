n=input()
import itertools as it
n=list(it.permutations(n))
for i in n:
    i=list(i)
    for j in i:
        print(j,end="")
    print()