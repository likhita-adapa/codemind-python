n=input()
vowel = 'aeiouAEIOU'

c=[]

for i in range(0,len(n)-1):
    
    if n[i] not in vowel and n[i+1] not in vowel:
        continue
    
    if n[i] in vowel and n[i+1] in vowel:
        continue
    
    if n[i] not in vowel:
        c.append('C')
    else:
        c.append('V')
        
if n[-1] not in vowel:
    c.append('C')
else:
    c.append('V')
        
print(''.join(c))
        