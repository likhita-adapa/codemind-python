s=input()
i=0
j=len(s)
for k in s:
    if k=='I':
        print(i,end=' ')
        i+=1
    if k=='D':
        print(j,end=' ')
        j-=1
print(i)