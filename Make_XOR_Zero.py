def xored(arr, data, add, n):
    res = 0
    for i in arr:
        res ^= ((i + data) & add)
    return res;

def solve(arr, n):
    add = 1
    res = 0
    maxim = max(arr)
    while add <= maxim:
        xr = xored(arr, res, add, n)
        if xr != 0:
            res += add
        add += 1
    xr = 0
    for i in arr:
        xr ^= (i + res)
    if xr == 0:
        return res
    return -1
n = int(input())
arr = list(map(int, input().split()))
print(solve(arr, n))


