# cook your dish here
def TailCount(n):
    li= list(str(n))
    li.reverse()
    count= 0
    for i in range (len(li)):
        if(int(li[i])==0):
            count+=1 
        else:
            return count
    return count

n= int(input())
print(TailCount(n))