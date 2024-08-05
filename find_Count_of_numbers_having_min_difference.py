# cook your dish here
def findCount(arr, length, num, diff):
    a=[]
    for i in range(length):
        if abs(num-arr[i]) <= diff:
            a.append(arr[i])
    l= len(a)
    return l
    
arr= list(map(int, input().split()))
length = int(input())
num= int(input())
diff= int(input())
print(findCount(arr, length, num, diff))