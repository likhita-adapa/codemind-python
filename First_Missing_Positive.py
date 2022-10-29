n=int(input())
l=list(map(int,input().split()))
i=1
while True:
    if i not in l:
        print(i)
        break
    else:
        i+=1