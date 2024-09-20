def DigitSumDifference(m, n):
    four=0
    seven=0
    for i in range(m,n+1):
        if i%4==0 and i%7==0:
            while(i!=0):
                four+=i%10
                seven+=i%10
                i//=10
        elif i%4==0:
            while(i!=0):
                four+=i%10
                i//=10
        elif i%7 == 0:
            while(i!=0):
                seven+=i%10
                i//=10
    return abs(four-seven)

m=int(input())
n= int(input())
print(DigitSumDifference(m, n))