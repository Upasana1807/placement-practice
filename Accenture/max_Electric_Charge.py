# cook your dish here
def maxElectricCharge(mag, charge, n):
    sum=0
    for i in range (n):
        if charge [i] == 'P':
            sum+= mag[i]
        else:
            sum-= mag[i]
    return (sum*100)

mag= list(map(int, input().split()))
charge= input()
n= int(input())
print(maxElectricCharge(mag, charge, n))