s=input()
x=input()
c=0
p=0
for i in range(len(s)):
    if x ==s[i]:
        c=1
        p=i
        break
if c==1:
    print('True')
    print(p)
else:
    print('False')
    