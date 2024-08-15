# cook your dish here
def SumOfDivisors(n):
    a=0
    for i in range(1, n+1, 1):
        if n%i == 0:
            a+=i
    return a
    

n= int(input())
print(SumOfDivisors(n))