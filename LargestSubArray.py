# cook your dish here
def LargestSubArray(n, arr):
    if(arr.count(0) == 0) or (arr.count(1) ==0):
        return 0 
    else:
        return (min(arr.count(0), arr.count(1))*2)

n= int(input())
arr= list(map(int, input().split()))
print(LargestSubArray(n, arr))