# cook your dish here
def MaxLargest(arr):
    li= list(map(str,arr))
    li= ''.join(li)
    li= sorted(li)
    li.reverse()    
    li= ''.join(li)
    return li

arr=list(map(int,input().split())) 
print(MaxLargest(arr))