def PalindromeCheck(str):
    str=list(str)
    str1= str[::-1]
    if str == str1:
        return True
    else:
        return False

str= input()
print(PalindromeCheck(str))