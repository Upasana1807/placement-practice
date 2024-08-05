# cook your dish here
def MoveHyphen(arr, n):
    if(n<1):
        return None
    a=[]
    h= arr.count('-')
    for i in range(n):
        if arr[i] != '-':
            a.append(arr[i])
    arr=['-']*h +a 
    arr= ''.join(arr)
    return arr
arr= input()
n = int(input())
print(MoveHyphen(arr, n))