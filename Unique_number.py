n=int(input())
Ist=[]
r=0
while n!=0:
    r=n%10
    Ist.append(r)
    n=n//10
if len(set(Ist))==len(Ist):
    print("Unique Number")
else:
    print("Not Unique Number")   