s=input()
a1=list(s.split(","))
for i in a1:
    a2=list(i.split(":"))
    n1=a2[0]
    n2=a2[1]
    m='0'
    for i in n2:
        if ord(i)>ord(m):
            if ord(i)-48<=len(n1):
                m=i
    ind=ord(m)-48
    name10=n1*10
    if m=='0':
        print("X",end="")
    else:
        print(name10[ind-1],end="")