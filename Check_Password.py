def checkPassword(str,n):
    if len(str) < 4 or str[0].isdigit():
        return 0
    else:
        count=0
        flag=0
        for i in range(len(str)):
            if str[i]=='/' or str[i]==' ':
                return 0
            elif str[i].isupper():
                count+=1
            elif str[i].isdigit():
                flag+=1
        if count and flag:
            return 1

str=input()
n= int(input())
print(checkPassword(str,n))