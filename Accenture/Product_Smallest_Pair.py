# cook your dish here
def ProductSmallestPair(sum, arr):
    if (len(arr) == 0) or (len(arr)<2):
        return -1
    else:
        arr= sorted(arr)
    if arr[0]+arr[1] <= sum:
        return (arr[0]*arr[1])
    else:
        return 0

sum= int(input())
arr= set(map(int,input().split()))
print(ProductSmallestPair(sum, arr))



# def ProductSmallestPair(sum, arr):
#     if (len(arr) == 0) or (len(arr)<2):
#         return -1
#     else:
#         arr.sort()
#     if arr[0]+arr[1] <= sum:
#         return (arr[0]*arr[1])
#     else:
#         return 0

# sum= int(input())
# arr= list(map(int,input().split()))
# print(ProductSmallestPair(sum, arr))

