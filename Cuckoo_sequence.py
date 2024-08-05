# cook your dish here
def CuckooSequence(n):
    Cuckoo=0
    for i in range(1, n, 1):
        mul= i*(n-i)
        Cuckoo+= mul
    return Cuckoo

n= int(input())
print(CuckooSequence(n))