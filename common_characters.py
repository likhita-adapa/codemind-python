s1=input().lower()
s2=input().lower()
c=0
s=''
l=list(set(s1)&set(s2))
for i in l:
    if i==' ':
        continue
    s+=i
    c=1
x=sorted(s)
if c==0:
    print('-1')
else:
    for i in x:
        print(i,end='')