x = list(map(str,input().split()))
a='AEIOUaeiou'
m=[]
for i in x:
    for j in i:
        if j not in a:
            m.append(j)
    m.sort()
    k=0
    for j in range(len(i)):
        if i[j] in a:
            print(i[j],end="")
        else:
            print(m[k],end="")
            k+=1
    m.clear()
    print(end=" ")