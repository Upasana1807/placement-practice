def sumOfEvenIndexedOfReversedarray (a, n):
    a.reverse()
    sum=0
    for i in range(n):
        if i%2 ==0:
            sum+= a[i]
    return sum


a= list(map(int, input().split()))
n= int(input())
print(sumOfEvenIndexedOfReversedarray (a, n))