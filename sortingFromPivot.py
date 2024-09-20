def SortingFromPivot (len, arr, n):
    arr1= arr[:n]
    arr1.sort()
    arr= arr[n:]
    arr.sort(reverse= True)    
    return ' '.join(map(str, arr1+arr))

len= int(input())
arr= list(map(int, input().split()))
n= int(input())
print(SortingFromPivot(len, arr, n))