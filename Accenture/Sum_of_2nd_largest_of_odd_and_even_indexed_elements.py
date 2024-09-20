# cook your dish here
length= int(input())
arr= list(map(int, input().split()))
if((len(arr)==0) or (length==0)):
    print("0")
else:
    a=[]
    b=[]
    for i in range(length):
        if(i%2==0):
            a.append(arr[i])
        else:
            b.append(arr[i])
print(a[-2]+b[-2])