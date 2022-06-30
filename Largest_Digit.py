n=int(input())
max=0
while n>0:
    dig=n%10
    if max<dig:
        max=dig
    n=n//10
print(max)      