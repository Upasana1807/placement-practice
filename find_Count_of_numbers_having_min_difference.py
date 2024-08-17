# cook your dish here
def findCount(arr, num, diff):
    a=0
    for i in arr:
        if abs(num-i) <= diff:
            a+=1
    if a:
        return a
    else:
        return -1
    
arr= list(map(int, input().split()))
num= int(input())
diff= int(input())
print(findCount(arr, num, diff))