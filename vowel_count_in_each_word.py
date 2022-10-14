n=input()
z=n.split()
for i in z:
    vowel=sum(letter in'aeiou' for letter in i.lower())
    print(vowel,end=" ")