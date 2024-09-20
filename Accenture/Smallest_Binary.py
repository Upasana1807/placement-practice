# cook your dish here
def SmallestBinary(n):
    n= bin(n)
    binary=list(n)
    binary= binary[2:]
    binary.sort()
    binary= ''.join(binary)
    binary= int(binary,2)
    return binary


n= int(input())
print(SmallestBinary(n))