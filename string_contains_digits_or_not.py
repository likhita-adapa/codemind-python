t=int(input())
count=0
while t>0:
    s=str(input())
    count=0
    for charecter in s:
        if charecter.isdigit():
            count=count+1
    if(count>0):
        print("Yes")
    else:
        print("No")
        t=t-1