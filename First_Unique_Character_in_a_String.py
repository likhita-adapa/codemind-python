s=input()
for i in range(0,len(s)):
    r=0
    for j in range(0,len(s)):
        if(s[i]==s[j] and j!=i):
            r-=1
    if r==0:
        print(i)
        break
else:
    print('-1')
    