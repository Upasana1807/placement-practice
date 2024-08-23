def minElementIndex (arr):   
    return min(arr), arr.index(min(arr))

arr= list(map(int, input().split()))
print(minElementIndex (arr))
