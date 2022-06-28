s=input()
c=0
for i in s:
    if(i.isdigit()):
        c=c+1
if(c>0):
    print("Contains",c,"digit")
else:
    print("Doesn't contain digit")