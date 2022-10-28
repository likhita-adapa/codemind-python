n=int(input())

l=list(map(int,input().split()))

p, d = -float("inf"), 0

for i in l:
    
    a, b = p, d
    
    p = max( a, b - i )
    
    d = max( b, a + i )
    
print(d)