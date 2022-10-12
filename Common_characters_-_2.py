s=input().lower()
s=s.split(' ')
x=''
l=len(s)
c=0
for i in range(len(s[0])):
    count=0
    for j in range(l):
        if s[0][i] in s[j]:
            count+=1
    if count==l:
        c+=1
print(c)