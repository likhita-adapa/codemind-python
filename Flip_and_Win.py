n=int(input())
s=input()
a=0
i=0
while i<n-1:
    a+=abs(int(s[i+1])-int(s[i]))
    i+=1
a=n-a-1
if(a%3==0):
    print('Sudhir')
else:
    print('Ashok')