s=input()
l=[]
f=1
for i in range(len(s)):
    if s[i] in '({[':
        l.append(s[i])
        f=1
    else:
        if len(l)>0:
            if l[-1]=='(' and s[i]==')':
                l.pop()
            elif l[-1]=='{' and s[i]=='}':
                l.pop()
            elif l[-1]=='[' and s[i]==']':
                l.pop()
            else:
                print(i+1)
                f=0
                break
        else:
            print(i+1)
            f=0
            break
if f==1:
    if(len(l)==0):
        print(0)
    else:
        print(len(s)+1)
