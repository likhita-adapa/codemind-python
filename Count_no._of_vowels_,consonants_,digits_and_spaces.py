s=input()
k=0
v=0
m=0
a=0
i=0
while i<len(s):
    if s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U' or s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o'or s[i]=='u':
        k+=1
    elif s[i]>='0' and s[i]<='9':
        v+=1
    elif s[i]==' ':
        m+=1
    else:
        a+=1
    i+=1
print("Vowels: %d" %k)
print("Consonants: %d"%a)
print("Digits: %d"%v)
print("White spaces: %d"%m)
