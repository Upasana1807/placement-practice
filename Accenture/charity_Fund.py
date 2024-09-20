# cook your dish here
def charityFund(n):
    a=0
    for i in range(1, n+1, 1):
        a+= i**2
    return a
    

n= int(input())
print(charityFund(n))