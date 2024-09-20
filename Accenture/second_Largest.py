# cook your dish here
def secondLargest(n, arr):
    arr= set(arr)
    if(len(arr)<2):
        return -1
    else:
        arr= sorted(arr)
        return arr[-2]
    

n= int(input())
arr= list(map(int, input().split()))
print(secondLargest(n, arr))