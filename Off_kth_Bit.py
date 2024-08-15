# cook your dish here
def OffkthBit(n, k):
    n= bin(n)
    li= list(n)
    li= li[2:]
    if li[-k] == 0:
        return n
    else:
        li[-k]= '0'
        li= ''.join(li)
        li= int(li,2)
        return li

n= int(input())
k= int(input())
print(OffkthBit(n, k))