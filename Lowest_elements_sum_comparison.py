# cook your dish here
sum=int(input())
n=int(input())
arr=list(map(int, input().split()))
if((len(arr)==0) or (n<2)):
    print(-1)
else:
    arr.sort()
    if((arr[0]+arr[1])<=sum) :
        print(arr[0]*arr[1])
    else:
        print("0")