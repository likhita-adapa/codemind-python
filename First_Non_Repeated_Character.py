t=int(input())
for k in range(t):
    a=int(input())
    s=input()
    c=co=0
    for i in s:
        c=0
        for j in s:
            if i==j:
                c+=1
        if c==1:
            print(i)
            co=1
            break
    if co==0:
        print(-1)