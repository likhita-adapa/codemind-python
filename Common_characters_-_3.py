s=input().lower()
s=s.split(' ')
l=len(s)
c=0
x=''
for i in range(len(s[0])):
    count=0
    for j in range(l):
        if s[0][i] in s[j]:
            count+=1
    if count==l:
        x+=s[0][i]
        c=1
if c==0:
    print('-1')
else:
    print(min(x))