s=input()
count=0
for charecter in s:
    if charecter.isdigit():
        count=count+int(charecter)
print(count)           