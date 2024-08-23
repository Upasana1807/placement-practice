def ReverseWords(str):
    str= list(str)    
    return ''.join(str[::-1])

str= input()
print(ReverseWords(str))