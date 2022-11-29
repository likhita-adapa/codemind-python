s=input()
s=s.split()
m=0
l=0
diff=0
for words in s:
    a=min(words)
    b=max(words)
    m=m+ord(a)
    l=l+ord(b)
diff=abs(m-l)
print(diff)