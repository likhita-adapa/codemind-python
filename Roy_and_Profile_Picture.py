l=int(input())
n=int(input())
i=0
while i<n:
    wh=(input().split())
    w=int(wh[0])
    h=int(wh[1])
    if w<l or h<l:
        print("UPLOAD ANOTHER")
    else:
        if w==h and (w>=1 and h>=1):
            print("ACCEPTED")
        else:
            print("CROP IT")