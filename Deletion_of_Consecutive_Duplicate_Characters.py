x=int(input())
for i in range(x):
    s=input()
    n=len(s)
    c=0
    for j in range(len(s)-1):
        if s[j]==s[j+1]:
            c+=1
    print(c)