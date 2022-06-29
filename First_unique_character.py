s=input()
for i in s:
    c=s.count(i)
    if c==1:
        print(i)
        break
else:
    print('-1')
 