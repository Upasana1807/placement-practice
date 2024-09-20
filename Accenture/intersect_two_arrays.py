l1= list(input().split())
l2= list(input().split())
arr=[]
for i in l1:
    for j in l2:
        if(i==j):
            arr.append(i)
print(arr)