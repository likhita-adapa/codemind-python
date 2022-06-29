n=int(input())
a=list(map(int,input().split()))
s=sorted(list(set(a)))
print(s[len(s)-3])
