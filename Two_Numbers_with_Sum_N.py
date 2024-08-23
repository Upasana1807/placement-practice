def TwoNumberswithSumN (arr, n):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr))        :
            if arr[i]+ arr[j] == n:
               return (arr[i], arr[j])
    return -1
    

arr= list(map(int, input().split()))
n= int(input())
print(TwoNumberswithSumN (arr, n))