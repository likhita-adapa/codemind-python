x = list(map(str,input().split()))
a='~!@#$%^&*()_-`?.,<>{}[]'
m=[]
for i in x:
    for j in i:
        if j not in a:
            m.append(j)
    m.sort()
    k=0
    for j in i:
        if j in a:
            print(j,end="")
        else:
            print(m[k],end="")
            k+=1
    print(end=" ")
    m.clear()