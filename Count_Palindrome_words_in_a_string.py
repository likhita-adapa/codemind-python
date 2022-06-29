def Pal(s):
    if s.lower() == s.lower()[::-1]:
        return True
def countPal(str):
    count = 0
    l=str.split(" ")
    for i in l:
        if (Pal(i)):
            count += 1
    print (count)
s=input()
countPal(s)
