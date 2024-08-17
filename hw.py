def DectoNBase(n, num):
    rem=[]
    while num!=0:
        rem.append(num%n)
        num//=n
    rem.reverse()
    for i in range(len(rem)):
        if rem[i]>9:
            rem[i]= chr(rem[i]+55)
        else:
            rem[i] = str(rem[i])
    return ''.join(rem)

n= int(input())
num= int(input())
print(DectoNBase(n, num))


def MoveHyphen(str,n):
    if n==0:
        return None
    else:
        h= str.count('-')
        a=[]
        for i in range(n):
            if str[i] != '-':
                a.append(str[i])
        a= ''.join(a)
        a= '-'*h +a
    return ''.join(a)

str= input()
n= int(input())
print(MoveHyphen(str,n))