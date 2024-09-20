def CharacterReplacement(str, ch1, ch2):
    str= ((str.replace(ch1,'*')).replace(ch2 , ch1)).replace('*', ch2)    
    return str

str= input()
ch1 = input()
ch2= input()
print(CharacterReplacement(str, ch1, ch2))