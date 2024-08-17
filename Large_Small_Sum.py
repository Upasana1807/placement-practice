def LargeSmallSum(arr):
    if len(arr) == 0 or len(arr) <= 3:
        return 0
    else:
        o=[]
        e=[]
        for i in range(len(arr)):
            if i%2== 0:
                e.append(arr[i])
            else:
                o.append(arr[i])
        o.sort()
        e.sort()
    return e[-2]+o[1]

arr= list(map(int, input().split()))
print(LargeSmallSum(arr))