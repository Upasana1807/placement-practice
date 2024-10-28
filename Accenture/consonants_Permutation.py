# import math
def consoPermutation (s):
    count=0
    vowel=['a', 'e', 'i', 'o', 'u']
    for i in range(len(s)):
        if s[i] not in vowel:
            count+=1
    if count== 0:
        return 0
    else:
        facto= 1
        while(count!=0):
            facto*= count
            count-=1
        return facto
    
s= input()
print(consoPermutation (s))