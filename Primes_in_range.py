def prime(i):
    if i == 1:
        return 0
    for j in range(2,int((i**0.5)+1)):
        if i%j==0:
            return 0
    return 1

x = int(input())
y = int(input())
c=0
for i in range(x,y+1):
    if prime(i):
        c+=1
if c==0:
    print('-1')
else:
    print(c)