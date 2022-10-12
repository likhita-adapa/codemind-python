x = list(map(str,input().split()))
for i in x:
    s,m=0,0
    s+=ord(max(i))
    m+=ord(min(i))
    print(s-m,end=" ")