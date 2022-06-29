def Missing(a):
    n=len(a)
    total = (n + 1)*(n + 2)/2
    sumofa= sum(a)
    return total-sumofa
n=int(input())
for i in range(n):
    x=int(input())
    a=list(map(int,input().split()))
    print(int(Missing(a)))
