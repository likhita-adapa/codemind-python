s=input()
c=0
c1=0
v='aeiou'
for i in range(len(s)):
    if s[i]=='a' or s[i]=='e' or s[i]=='o' or s[i]=='u' or s[i]=='i':
        c+=1
    else:
        if c1<c:
            c1=c
        c=0
if c1<c:
    c1=c
print(c1)