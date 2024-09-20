# cook your dish here
def rat_food(r, unit, n, arr):
    if len(arr)==0:
        return -1
    else:
        sum= 0
        for i in range(n):
            sum+=arr[i]
            if (r*unit)<= sum:
                return (i+1)
        if (r*unit)> sum:
            return 0
        
        

        
r=int(input())
unit= int(input())
n= int(input())
arr= list(map(int, input().split()))
print(rat_food(r, unit, n, arr))