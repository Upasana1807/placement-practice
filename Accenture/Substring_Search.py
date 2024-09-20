def SubstringSearch(str1, str2):
    if str2 not in str1:
        return -1
    else:
        return str1.find(str2)
     

str1= input()
str2= input()
print(SubstringSearch(str1, str2))