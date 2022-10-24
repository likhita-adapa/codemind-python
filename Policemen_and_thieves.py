n=int(input())
for p in range(n):
    a,b=map(int,input().split())
    c=0
    for i in range(a):
        s=input()
        l=[]
        for j in s:
            if j=='P' or j=='T':
                l.append(j)
        for j in range(a):
            if l[j]=='P':
                for k in range(a):
                    if l[k]=='T':
                        if abs(k-j)<=b:
                            c+=1
                            l[k]='0';
                            break
                continue
print(c)