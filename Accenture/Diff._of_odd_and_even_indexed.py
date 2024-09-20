# cook your dish here
n= int(input())
m= int(input())
sum=0
total= 0 
for i in range(1,m+1,1):
    if(i%n==0):
        sum+=i
    else:
        total +=i
print(abs(total-sum))