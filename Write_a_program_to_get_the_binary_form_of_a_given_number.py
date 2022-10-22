l=[]
for i in range(int(input())):
    n=int(input())
    s=bin(n)
    l.append(s[2:])
for i in l:
    print(i)