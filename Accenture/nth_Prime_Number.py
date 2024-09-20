# cook your dish here
def nthPrimeNumber(n):
    n1= n
    num= 1 
    a=[]
    while(n>=0):
        count=0
        for i in range(2, (num//2)+1, 1):
            if num%i == 0:
                count+=1
        if(num==2) or (count==0 and num!=1):
            a.append(num)
            n-=1
        num+=1
    return a[n1-1]

n= int(input())
print(nthPrimeNumber(n))