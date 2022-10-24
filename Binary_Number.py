n=int(input())
i=1
h=''
for j in range(n):
    h+='0'
print(h)
while True:
    m=bin(i)
    m=m[2:]
    n_l = len(m)
    t_l = n-n_l
    if n_l<=n:
        if t_l <=0:
            pass
        for j in range(t_l):
            m='0'+m
        print(m)
    if n_l>n:
        break
    i+=1