n1=int(input())
for i in range(0,n1):
    s=input()
    r=0
    for i in range(1,len(s)):
        if(ord(s[i])>=48 and ord(s[i])<=57):
            r+=1
    if(r==len(s)-1):
        print(True)
    else:
        print(False)