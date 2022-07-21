x = list(map(str,input().split()))
a ='aeiouAEIOU'
c=0
d=0
for i in x:
    for j in range(len(i)//2):
        if ((i[j] in a) and (i[len(i)-j-1] not in a)) or ((i[j] not in a) and (i[len(i)-j-1] in a)):
            c+=1
print(c)