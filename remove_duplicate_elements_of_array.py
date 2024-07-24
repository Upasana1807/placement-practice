l1= list(input().split())
arr=[]
for i in l1:
    if i not in arr:
        arr.append(i)
print(arr)