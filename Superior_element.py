def superior_element(n, arr):
    count =1
    for i in range(n-1):
        a= arr[i+1:]
        if arr[i] > max(a):
            count +=1        
    return count

n= int(input())
arr= list(map(int, input().split()))
print(superior_element(n, arr))
