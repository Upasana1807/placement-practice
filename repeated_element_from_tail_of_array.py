def RepeatedNumbers (arr, n):
    arr.reverse()
    count=0
    for i in arr:
        if i<=0:
            count+=1
    if count == n:
        return 0
    else:
        for i in arr:
            if i>0:
                if arr.count(i) > 1:
                    return i
        return arr[0]
    

arr= list(map(int, input().split()))
n= int(input())
print(RepeatedNumbers (arr, n))