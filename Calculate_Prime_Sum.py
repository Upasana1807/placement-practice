def CalculatePrimeSum (m,n):
    sum=0
    for i in range(m,n+1):
        count=0
        for j in range(2, i//2+1):
            if i%j == 0:
                count+=1
        if (count==0 or i==2) and (i!=1):
            sum+=i            
    return sum

m= int(input())
n= int(input())
print(CalculatePrimeSum (m,n))