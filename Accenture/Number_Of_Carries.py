# cook your dish here
def NumberOfCarries(num1, num2):
    count =0
    carry=0
    l= max(num1, num2)
    while(l !=0):
        if ((num1%10) + (num2%10) + carry) > 9:
            count+=1
            carry= 1
        else:
            carry=0
        num1 //= 10
        num2 //= 10
        l//= 10
    return count
num1= int(input())
num2= int(input())
print(NumberOfCarries(num1, num2))