s=input()
l=list(s)
alp=[]
spe=[]
spei=[]
for i in range(len(l)):
    if l[i].isalpha():
        alp.append(l[i])
    else:
        spe.append(l[i])
        spei.append(i)
rev=alp[::-1]
for i in range((len(spei))):
    rev.insert(spei[i],spe[i])
print(*rev,sep='')