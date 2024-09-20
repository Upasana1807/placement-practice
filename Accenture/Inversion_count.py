# cook your dish here
def Inversioncount(a, n):
    if len(a) == 0:
        return -1
    elif n<2 :
        return 0
    else:
        count= 0
        for i in range(n-1):
            for j in range(i+1, n,1):
                if(a[i]>a[j]):
                    count+=1
    return count

a= list(map(int, input().split()))
n= int(input())
print(Inversioncount(a, n))