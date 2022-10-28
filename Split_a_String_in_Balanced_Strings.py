a=input()
arr=[]
c=0
for i in range(len(a)):
    rc=lc=0
    ind=0
    for j in range(i):
        if a[j]=='R':
            rc+=1
        if a[j]=='L':
            lc+=1
        ind=j
    if rc==lc:
        c+=1
print(c)