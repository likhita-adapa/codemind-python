s1=input().lower()
s2=input().lower()
s3=s1.split(' ')
s4=s2.split(' ')
c=0
for i in range(0,len(s3)):
    if s3[i] in s4 and s1.count(s3[i])==s2.count(s3[i]):
        c+=1
print(c)