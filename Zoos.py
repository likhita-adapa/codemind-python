s=input()
r=0
k=0
for i in range(0,len(s)):
    if(s[i]=='z' or s[i]=='z'):
        r+=1
    elif(s[i]=='o' or s[i]=='o'):
        k+=1
if(2*r==k):
    print('Yes')
else:
    print('No')