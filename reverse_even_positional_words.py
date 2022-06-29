s=list(map(str,input().split()))
for i in range(len(s)):
    if i%2==0:
        print((s[i])[::-1],end=' ')
    else:
        print(s[i],end=' ')