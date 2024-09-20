def averageOfAllPositives(arr):
    count=0
    sum=0
    for i in arr:
        if i>=0:
            count+=1
            sum+=i
    if count :
        return round(sum/ count)
    else:        
        return -1

arr= list(map(int,input().split()))
print(averageOfAllPositives(arr))