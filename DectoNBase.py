# cook your dish here
def DectoNBase(num, n):
    arr=[]
    while(num>0):
        arr.append(num%n)
        num= num//n
    arr.reverse()
    a=[]
    for i in range(len(arr)):
        if arr[i] <= 9:
            a.append(str(arr[i]))
        else:
            a.append(chr(arr[i]+55))
    a= ''.join(a)
    return a
n = int(input())
num= int(input())
print(DectoNBase(num, n))