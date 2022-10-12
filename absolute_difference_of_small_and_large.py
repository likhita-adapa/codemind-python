s=input()
s=s.split(' ')
for i in s:
    print(abs(ord(min(i))-ord(max(i))),end=' ')