x = int(input())
l = list(map(int,input().split()))
y = int(input())
for i in range(x):
    if l[i]==y:
        print(i)
        break
else:
    print('-1')