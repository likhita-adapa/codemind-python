s=input()
v='aeiouAEIOU'
c=0
for i in sorted(set(s),key=s.index):
    if i in v:
        c+=1
        print(i,end=' ')
if c==0:
    print('-1')