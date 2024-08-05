# cook your dish here
def InterestingNumbers(start, end):
    count=0
    for i in range(start, end+1, 1):
        a=0
        for j in range(1, i+1, 1):
            if i%j == 0:
                a+=1
        if (a%2):
            count+=1
    return count

start=int(input())
end= int(input())
print(InterestingNumbers(start, end))