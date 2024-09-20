def LuckyNumber (n):
    n= bin(n)
    li= list(str(n))
    li=li[2::]
    if len(li)%2 :
        li.insert(0, '0')
    i=0
    while(i< len(li)):
        li[i], li[i+1] = li[i+1], li[i]
        i+=2
    return int(''.join(li),2)

n= int(input())
print(LuckyNumber (n))