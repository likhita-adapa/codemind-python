x = input()
l = ['A','E','I','O','U','a','e','i','o','u']
s=0
for i in x:
    if i in l:
        s+=1
print(s)