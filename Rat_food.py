# cook your dish here
r=int(input())
unit= int(input())
n= int(input())
arr= list(map(int, input().split()))
sum=0
for i in range(n):
    sum+=arr[i]
    if((r*unit)<=sum):
        print(i+1)
        break