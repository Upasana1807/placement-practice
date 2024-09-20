# cook your dish here
def differenceofSum(n,m):
    d=0
    non=0
    for i in range(1,m+1,1):
        if i%n==0:
            d+=i
        else:
            non+=i
    return (non-d)

n= int(input())
m= int(input())
print(differenceofSum(n,m))


