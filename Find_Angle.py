import math
a=int(input())
b=int(input())
hyp=math.sqrt(a*a+b*b)
hyp=hyp/2
a=a/2
angle=round(math.degrees(math.acos(a/hyp)))
print(angle)