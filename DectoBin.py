# def DecimalToBinary(num):
    
#     return bin(num).replace("0b", "")

# num= int(input())
# print(DecimalToBinary(num))



def BinaryToDecimal(num):
    
    return (int(num, 2))

num= input()
print(BinaryToDecimal(num))