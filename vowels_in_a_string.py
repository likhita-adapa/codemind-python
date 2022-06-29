s=input()
ch=input()
f=0
m=0
for i in range(len(s)):
    if s[i] in ch:
        f=1
if f==1:
    print('True')
    print(s.index(ch))
else:
    print('False')