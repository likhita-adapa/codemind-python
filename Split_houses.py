n = int(input())
s = input()
c = []
temp = 0
arr = ['']*n
for i,j in enumerate(s):
    if j == 'H':
        arr[i] = 'H'
        temp += 1 
        if i == n-1:
            c.append(temp)
    else:
        arr[i] = 'B'
        if temp > 0:
            c.append(temp)
            temp = 0

if len(c) == 0 or max(c) == 1:
    print('YES')
    print(''.join(arr))
else:
    print('NO')