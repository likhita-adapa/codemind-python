def rev(x):
    a = x
    s=0
    while x!=0:
        v = x%10
        s = s*10+v
        x = x//10
    n = a+s
    m = str(n)
    if str(n)==m[ :: -1]:
        print(n)
    else:
        rev(n)
    
x = int(input())
rev(x)