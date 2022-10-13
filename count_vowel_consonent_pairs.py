s=input()
s=s.lower()
c=0
v="aeiou"
a,b=0,len(s)-1
while a<b:
    if s[a].isalpha() and s[b].isalpha():
        if ( s[a] in v and s[b] not in v) or (s[a] not in v and s[b] in v):
            c+=1
    a+=1
    b-=1
print(c)