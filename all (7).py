# cook your dish here
def NumberOfCarries(num1, num2):
    num1= list(str(num1))
    num2= list(str(num2))
    l= max(len(num1), len(num2))
    num1.reverse()
    num2.reverse()
    carry=0
    for i in range(l):
        if int(num1[i])+ int(num2[i]) >9 :
            carry+=1
            int(num1[i+1])+1
    return carry
    

num1= int(input())
num2= int(input())
print(NumberOfCarries(num1, num2))