def EvenOddLabeling (a, n):
    s=''
    for i in a:
        if i%2:
            s+='Odd'
        else:
            s+='Even'
    return s

a= list(map(int, input().split()))
n= int(input())
print(EvenOddLabeling (a, n))