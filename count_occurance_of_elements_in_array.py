arr= list(map(int, input().split()))
a=[]
for k in arr:
    if k not in a:
        a.append(k)
for i in a:
    count=0
    for j in arr:
        if(i==j):
            count+=1 
    print(f"{i} = {count}")
    