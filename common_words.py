s1=input().lower()
s2=input().lower()
s1=s1.split(' ')
s2=s2.split(' ')
for i in s2:
    for j in s1:
        if i==j:
            print(i,end=' ')