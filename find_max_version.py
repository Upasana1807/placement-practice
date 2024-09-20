def findMaxVersion (s, n):
    if n<=0:
        return -1
    else:
        a=0
        for i in s:
            if i[5:].isdigit() and i[:5] == 'File_':
                a= max(a, int(i[5:]))
        if a:
            return a
        else:
            return -1
    

s= list(input().split())
n= int(input())
print(findMaxVersion(s, n))