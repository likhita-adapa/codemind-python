s=input()
s=s.lower()
s=s.replace(" ","")
c=0
for i in s:
    x=s.count(i)
    if x==1:
        c+=1
if c==0:
    print('-1')
else:
    print(c)