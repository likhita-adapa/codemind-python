n = input()
m = n.split(" ")
if len(m)==2:
    print(min(m[0]),max(m[1]))
else:
    print(min(m[0]),max(m[len(m)-2]))