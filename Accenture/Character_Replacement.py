def CharacterReplacement(str, ch1, ch2):
    str= ((str.replace('a','*')).replace('p','a')).replace('*','p')    
    return str

str= input()
ch1 = input()
ch2= input()
print(CharacterReplacement(str, ch1, ch2))