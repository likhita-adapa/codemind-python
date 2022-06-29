s=input()
c=0
c1=0
v='aeiou'
for i in s:
    if i in v:
        c+=1
    if i not in v:
        if c>c1:
            c1=c
        c=0
if c>c1:
    c1=c
print(c1)
