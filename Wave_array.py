x = int(input())
l = list(map(int,input().split()))
c=0
if l[0]<l[1]:
    if (l[x-2]<l[x-1] and l[x-1]>l[0]):
        c=1
    else:
        c=0
    for i in range(1,x-1,2):
        if (l[i-1]<l[i] and l[i]>l[i+1]):
            c=1
        else:
            c=0
            break
elif l[0]>l[1]:
    if (l[x-2]>l[x-1] and l[x-1]<l[0]):
        c=1
    else:
        c=0
    for i in range(1,x-1,2):
        if (l[i-1]>l[i] and l[i]<l[i+1]):
            c=1
        else:
            c=0
            break
if c==0:
    print('no')
else:
    print('yes')