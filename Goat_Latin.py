s=input().split()
v='AEIOUaeiou'
l=list(s)
for i in range(len(l)):
    s1=""
    if l[i][0] in v:
        s1=l[i]+'ma'
    else:
        s1=l[i][1:]+l[i][0]+'ma'
    for j in range(i+1):
        s1+='a'
    print(s1,end="")
    print("",end=" ")