n=int(input())
def add(n):
    return (n-1)%9+1 if n>0 else 0
print(add(n))